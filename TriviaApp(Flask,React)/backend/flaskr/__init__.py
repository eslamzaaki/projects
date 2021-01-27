import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
  : Set up CORS. Allow '*' for origins.
   Delete the sample route after completing the TODOs
  """
    CORS(app)

    ###################################################
    # Helper Functions
    ##################
    def category_format(categoriess):
        categories = {}
        for category in categoriess:
            categories[category.id] = category.type
        return categories

    def paging_questions(request):
        page = request.args.get("page", 1, type=int)
        index = page-1
        questions = Question.query.limit(QUESTIONS_PER_PAGE).offset(
            index*QUESTIONS_PER_PAGE).all()
        questions = [question.format() for question in questions]
        all_questions = Question.query.all()
        total_questions = len(all_questions)

        return questions, total_questions

    ###########################################
    """
  @: Use the after_request decorator to set Access-Control-Allow
  """

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Methods",
                             "GET,POST,DELETE,PATCH")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    """
  
  Create an endpoint to handle GET requests
  for all available categories.
  """

    @app.route("/categories")
    def retrive_categories():
        categoriess = Category.query.order_by(Category.id).all()
        categories = category_format(categoriess)
        return jsonify({"success": True, "categories": categories})

    


    @app.route("/questions")
    def get_paginated_questions():
        questions, total_questions = paging_questions(request)
        categoriess = Category.query.order_by(Category.id).all()
        categories = category_format(categoriess)

        if len(questions) == 0:  # page not found
            abort(404)

        return jsonify(
            {
                "success": True,
                "questions": questions,
                "total_questions": total_questions,
                "current_category": "1",
                "categories": categories,
            }
        )

 

    @app.route("/questions/<int:id>", methods=["DELETE"])
    def delete_question(id):
        question = Question.query.get(id)
        if question is None:  # not found the question to delete it
            abort(404)
        try:
            question.delete()
            return jsonify({"success": True})
        except:  # if server can't delete the question (not processable)
            abort(422)



    @app.route("/questions", methods=["POST"])
    def post_question():
        body = request.get_json()
        question = body.get("question", None)
        answer = body.get("answer", None)
        category = body.get("category", None)
        difficulty = body.get("difficulty", None)
        new_question = Question(
            answer=answer,
            question=question,
            difficulty=difficulty,
            category=category
        )
        try:
            new_question.insert()
            id = new_question.id
            return jsonify({"success": True, "question_id": id})
        except:
            abort(422)



    @app.route("/questions/search", methods=["POST"])
    def search_questions():
        searchTerm = request.get_json()["searchTerm"]
        questionss = Question.query.filter(
            Question.question.ilike("%{}%".format(searchTerm))
        )
        questions = [question.format() for question in questionss]
        total_questions = len(questions)
        current_category = "1"
        return jsonify(
            {
                "success": True,
                "questions": questions,
                "current_category": current_category,
                "total_questions": total_questions,
            }
        )

 

    @app.route("/categories/<int:category_id>/questions")
    def get_questions_by_Category(category_id):
        questionss = Question.query.filter(
            Question.category == str(category_id)).all()
        total_questions = len(questionss)
        current_category = str(category_id)
        questions = [question.format() for question in questionss]
        return jsonify(
            {
                "questions": questions,
                "total_questions": total_questions,
                "current_category": current_category,
                "success": True,
            }
        )

 

    @app.route("/quizzes", methods=["POST"])
    def play_quiz():
        previous_questions = request.get_json()["previous_questions"]
        quiz_category = request.get_json()["quiz_category"]
        category_id = quiz_category["id"]
        # case choose ALL from categories
        if category_id == 0:
            questions = Question.query.all()
        # case choose specific categroy
        else:
            questions = Question.query.filter(
                Question.category == category_id).all()
        questions = [question.format() for question in questions]
        # filter questions from previous questions
        questions = [
            question
            for question in questions
            if question["id"] not in previous_questions
        ]
        if questions != []:  # if questions had ended send False to frontend
            question = random.choice(questions)
        else:
            question = False
        return jsonify({"question": question, "success": True})

    """
 
 Create error handlers for all expected errors
 
  """

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "message": "not found",
            "error": 404}), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "message": "bad Request",
            "error": 400}), 400

    @app.errorhandler(422)
    def unprocessable(error):
        return
        jsonify({
            "success": False,
            "message": "unprocessable",
            "error": 422}), 422

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

    return app
