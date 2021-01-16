
from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website=db.Column(db.String(120))
    seeking_talent=db.Column(db.Boolean,default=False)
    talent_description=db.Column(db.String(600))
    shows=db.relationship('Show',backref='venue',lazy=True)
    

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    website =  db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue=db.Column(db.Boolean,default=False)
    seeking_description=db.Column(db.String(600))
    shows=db.relationship('Show',backref='artist',lazy=True)


    # TODO: implement any missing fields, as a database migration using Flask-Migrate
class Show(db.Model):
   __tablename__='shows'
   id = db.Column(db.Integer,db.Sequence('shows_id_seq'), primary_key=True,autoincrement=True)
   venue_id = db.Column(db.Integer,db.ForeignKey('Venue.id'),primary_key=True,) 
   artist_id=db.Column(db.Integer,db.ForeignKey('Artist.id'),primary_key=True)
   start_time=db.Column(db.DateTime)

