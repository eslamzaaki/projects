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


db_drop_and_create_all()

# ROUTES



@app.route('/drinks')
def get_drinks_public():
    drinks = Drink.query.all()
    drinks = [drink.short() for drink in drinks]
    return jsonify({
        "success": True,
        "drinks": drinks
    })



@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drinks_with_details(payload):
    drinks = Drink.query.all()
    drinks = [drink.long() for drink in drinks]
    return jsonify({
        "success": True,
        "drinks": drinks
    })




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




@app.errorhandler(AuthError)
def AuthError_handle(e):
    return jsonify({
        "success": False,
        "error": e.error['code'],
        "message": e.error['description'],
    }), e.status_code

