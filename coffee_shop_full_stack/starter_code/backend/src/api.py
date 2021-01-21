import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks')
def get_drinks_public():
    drinks = Drink.query.all()
    drinks = [drink.short() for drink in drinks]
    return jsonify({
        "success": True,
        "drinks": drinks
    })


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drinks_with_details(payload):
    drinks = Drink.query.all()
    drinks = [drink.long() for drink in drinks]
    return jsonify({
        "success": True,
        "drinks": drinks
    })


'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=["POST"])
@requires_auth('post:drinks')
def create_drink(payload):
    recipe = request.get_json()['recipe']
    title = request.get_json()['title']
    # check if title is  not repeated as title must be unique
    drinks = Drink.query.all()
    titles = [drink.title for drink in drinks]
    if title in titles:
        abort(400)
    drink = Drink(title=title, recipe=json.dumps(recipe))
    try:
        drink.insert()
        drink = [drink.long()]
        return jsonify({
            "success": True,
            "drinks": drink
        })
    except:
        abort(422)


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth("patch:drinks")
def modify_drink(payload, id):
    drink = Drink.query.get(id)
    if drink is None:  # if i can't find the drink
        abort(404)
    title = request.get_json()['title']
    try:
        drink.title = title
        drink.update()
    except:
        abort(400)
    finally:
        return jsonify({
            "success": True,
            "drinks": [drink.long()]
        })


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth("delete:drinks")
def delete_drink(payload, id):
    drink = Drink.query.get(id)
    if drink is None:  # if i can't find the drink
        abort(404)
    try:
        drink.delete()
    except:
        abort(422)
    finally:
        return jsonify({
            "success": True,
            "deleted": id
        })


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''


@app.errorhandler(404)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "not found"
    }), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "message": "bad Request",
        "error": 400}), 400


@app.errorhandler(500)
def internal_server_error(error):
    return
    jsonify(
        {"success": False,
         "message": "internal server error",
         "error": 500}
    ), 500


@app.errorhandler(405)
def Method_Not_Allowed(error):
    return
    jsonify(
        {"success": False,
         "message": "Method Not Allowed",
         "error": 405}
    ), 405


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''


@app.errorhandler(AuthError)
def AuthError_handle(e):
    return jsonify({
        "success": False,
        "error": e.error['code'],
        "message": e.error['description'],
    }), e.status_code

# https: // test460.us.auth0.com/authorize?response_type = token & client_id = 1nfR2801THLDVz2hCyiWp5CstHsXhezh & redirect_uri = http: // localhost: 8100 & audience = drink
