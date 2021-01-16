#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
import sys

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')

from models import db,Venue,Show,Artist
migrate = Migrate(app,db)
# TODO: connect to a local postgresql database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

   
   
  

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
  locals = []
  venues = Venue.query.all()
  for place in Venue.query.distinct(Venue.city, Venue.state).all():
      locals.append({
          'city': place.city,
          'state': place.state,
          'venues': [{
              'id': venue.id,
              'name': venue.name,
          } for venue in venues if
              venue.city == place.city and venue.state == place.state]
      })
  return render_template('pages/venues.html', areas=locals)
#------------------------------------------------------------------------------------------------#
@app.route('/venues/search', methods=['POST'])
def search_venues():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  search_term=request.form.get('search_term')
  queryy=Venue.query.filter(Venue.name.ilike('%'+search_term+'%'))#filer using ilike method
  count=queryy.count()
  venues=queryy.all() 
  data=[]
  for venue in venues:
    num=Show.query.filter(Show.venue_id==venue.id).filter(Show.start_time>datetime.now()).count()
    data.append({
      'id':venue.id,
      'name':venue.name,
      'num_upcoming_shows':num
    })
    
  response={
    'count':count,
    'data':data
  }
  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

#---------------------------------------------------------------------------------------------#

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  
  upcoming_shows=[]
  past_shows=[]
  venue=Venue.query.get(venue_id)# get venue by id from database
  past_showss=Show.query.join(Venue).filter(Venue.id==venue_id).filter(Show.start_time>datetime.now()).all()
  upcoming_showss=Show.query.join(Venue).filter(Venue.id==venue_id).filter(Show.start_time<datetime.now()).all()
  past_shows_count=len(past_showss) 
  upcoming_shows_count=len(upcoming_showss)
  #loop over all past shows to get past_shows object with exact format required 
  for past in past_showss:
    past_shows.append({
      "artist_id": past.artist_id,
      "artist_name":past.artist.name,
      "artist_image_link":past.artist.image_link,
      "start_time": str(past.start_time)
    })
  #loop over all upcoming shows to get upcoming_shows object with exact format required   
  for upcoming in upcoming_showss:
    upcoming_shows.append({
      "artist_id": upcoming.artist_id,
      "artist_name":upcoming.artist.name,
      "artist_image_link":upcoming.artist.image_link,
      "start_time": str(upcoming.start_time)
    })
  #get the exact format of data to send  
  data=venue
  data.upcoming_shows=upcoming_shows
  data.past_shows=past_shows
  data.past_shows_count=past_shows_count
  data.upcoming_shows_count=upcoming_shows_count    
  return render_template('pages/show_venue.html', venue=data)

#----------------------------------------------------------------------------------------------#
#  Create Venue
#  ------------------------------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)


@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
    form=VenueForm(request.form)
    error=False
    try:  #get data all data from form request
      venue=Venue()
      form.populate_obj(venue)
      if(request.form.get('seeking_talent')=='True'):
        venue.seeking_talent=True
      else:
        venue.seeking_talent=False  
      db.session.add(venue)
      db.session.commit()
      
    except: #case of error catched
      error=True
      db.session.rollback()
      print(sys.exc_info())
    finally:
      db.session.close()
    if error:
      flash('An error occurred. Venue ' + request.form['name']+ ' could not be listed.')
    else:
      flash('Venue ' + request.form['name'] + ' was successfully listed!')

    return render_template('pages/home.html')


  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion

  # on successful db insert, flash success
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
   

#---------------------------------------------------------------------------------------#
@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  error=False
  try:
    venue=Venue.query.get(venue_id)
    for show in venue.shows:
      db.session.delete(show)
    db.session.delete(venue)
    db.session.commit()
  except:
    db.session.rollback()
    error=True
  finally:
    db.session.close()
  if error:
    flash('fail Delete')
  else:
    flash('success Delete')           
  
  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
    return None

#---------------------------------------------------------------------------------
#  Artists
#  -----------------------------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database
  
  return render_template('pages/artists.html', artists=Artist.query.all())
#----------------------------------------------------------------------------------------
@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  search_term=request.form.get('search_term')
  queryy=Artist.query.filter(Venue.name.ilike('%'+search_term+'%'))
  count=queryy.count()
  artists=queryy.all()
  
  data=[]
  for artist in artists:
    num=Show.query.join(Artist).filter(Artist.id==artist.id).filter(Show.start_time>datetime.now()).count()
    data.append({
      'id':artist.id,
      'name':artist.name,
      'num_upcoming_shows':num
    })
    
    
  response={
    'count':count,
    'data':data
  }
  
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

#------------------------------------------------------------------------------------
@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  upcoming_shows=[]
  past_shows=[]
  artist=Artist.query.get(artist_id)
  past_showss=Show.query.join(Artist).filter(Artist.id==artist_id).filter(Show.start_time<datetime.now()).all()
  upcoming_showss=Show.query.join(Artist).filter(Artist.id==artist_id).filter(Show.start_time>datetime.now()).all()
  past_shows_count=len(past_showss)
  upcoming_shows_count=len(upcoming_showss)
  
  for past in past_showss:
    past_shows.append({
      "venue_id": past.venue_id,
      "venue_name":past.venue.name,
      "venue_image_link":past.venue.image_link,
      "start_time": str(past.start_time)
    })
  for upcoming in upcoming_showss:
    upcoming_shows.append({
      "venue_id": upcoming.venue_id,
      "venue_name":upcoming.venue.name,
      "venue_image_link":upcoming.venue.image_link,
      "start_time": str(upcoming.start_time)
    })
  data=artist
  data.upcoming_shows=upcoming_shows
  data.past_shows=past_shows
  data.past_shows_count=past_shows_count
  data.upcoming_shows_count=upcoming_shows_count
  return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist=Artist.query.get(artist_id)
  # TODO: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artist)
#-----------------------------------------------------------------------------------------

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes
  artist=Artist.query.get(artist_id)
  artist.name=request.form.get('name')
  artist.state=request.form.get('state')
  artist.city=request.form.get('city')
  artist.facebook_link=request.form.get('facebook_link')
  artist.phone=request.form.get('phone')
  artist.genres=request.form.get('genres')
  artist.address=request.form.get('address')
  db.session.commit()
  return redirect(url_for('show_artist', artist_id=artist_id))

#----------------------------------------------------------------------------------------------

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue=Venue.query.get(venue_id)
  # TODO: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venue)

#---------------------------------------------------------------------------------

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  venue=Venue.query.get(venue_id)
  venue.name=request.form.get('name')
  venue.state=request.form.get('state')
  venue.city=request.form.get('city')
  venue.facebook_link=request.form.get('facebook_link')
  venue.phone=request.form.get('phone')
  venue.genres=request.form.get('genres')
  venue.address=request.form.get('address')
  db.session.commit()
  return redirect(url_for('show_venue', venue_id=venue_id))
#----------------------------------------------------------------------
#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)
#-------------------------------------------------------------------------
@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  error=False
  form=ArtistForm(request.form)
  try: #get all parameters from form request
    artist=Artist()
    form.populate_obj(artist)    
    if(request.form.get('seeking_venue')=='True'):
      artist.seeking_venue=True
    else:
      artist.seeking_venue=False  
    db.session.add(artist)
    db.session.commit()
  except: #handle error case
    error=True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if error:
    flash('An error occurred. Artist ' + request.form['name']  + ' could not be listed.')
  else:
    flash('Artist ' + request.form['name'] + ' was successfully listed!')  
    
  return render_template('pages/home.html')
  
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  # on successful db insert, flash success
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
   


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
  #   
  #    num_shows should be aggregated based on number of upcoming shows per venue.
  shows=Show.query.all()
  data=[]
  for showw in shows:
    start_time=str(showw.start_time)# type cast datetime.datetime object into string
    data.append({
      'venue_id':showw.venue_id,
      'venue_name':showw.venue.name,
      'artist_id':showw.artist_id,
      'artist_name':showw.artist.name,
      'artist_image_link':showw.artist.image_link,
      'start_time':start_time
    })
  return render_template('pages/shows.html', shows=data)

#-----------------------------------------------------------------------------------
@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

#-------------------------------------------------------------------------------------
@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  error=False
  valid=0
  try:
    venue_id=request.form.get('venue_id')
    artist_id=request.form.get('artist_id')
    start_time=request.form.get('start_time')
    venues=Venue.query.all()
    artists= Artist.query.all()
    for venue in venues:
      print(venue.id)
      if venue_id==str(venue.id):
        valid+=1
    for artist in artists:
      print(artist.id)
      if artist_id==str(artist.id):
        valid+=1   
    if(valid!=2):
      flash('please Enter existent Venue ID and  Artist ID')
      return render_template('pages/home.html')
    
    show=Show(venue_id=venue_id,artist_id=artist_id,start_time=start_time)
    db.session.add(show)
    db.session.commit()
  except: #error case
    error=True
    db.session.rollback()
  finally:
    db.session.close()
  if error:
    flash('An error occurred. Show could not be listed.')
   
  else:
    flash('Show was successfully listed!')  
    

    return render_template('pages/home.html')
  

  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead
  # on successful db insert, flash success
  
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  
#***************************************************************************************************************
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
