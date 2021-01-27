import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Question, Category

DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'triviaapp')
DB_TEST_NAME = os.getenv('DB_TEST_NAME', 'trivia_test')


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = DB_TEST_NAME
        self.database_path = 'postgres://{}:{}@{}/{}'.format(
            DB_USER, DB_PASSWORD, DB_HOST, DB_TEST_NAME)
        setup_db(self.app, self.database_path)

        self.new_question = {
            "question": "what is ?",
            "answer": "yes",
            "category": "3",
            "difficulty": 2,
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

  

    # test retrive categories list
    def test_retrive_categories(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])

    # test retrive questions by page number
    def test_paginated_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertEqual(data["total_questions"], len(Question.query.all()))

    # test page not found error by request page number 1000
    def test_page_not_found(self):
        res = self.client().get("/questions?page=1000")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "not found")

    # test delete question Api
    def test_Delete_question(self):
        res = self.client().delete("/questions/2")
        data = json.loads(res.data)
        question = Question.query.get(2)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(question, None)

    # test delete question id  not found in database
    def test_Delete_question_not_found(self):
        res = self.client().delete("/questions/1100")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "not found")

    # test post new question
    def test_create_question(self):
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)
        id = data["question_id"]
        question = Question.query.get(id)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertNotEqual(question, None)

    # test get questions based on specific category
    def test_retrive_questions_by_category(self):
        res = self.client().get("/categories/1/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["total_questions"])
        self.assertEqual(data["current_category"], "1")

    # test search questions api
    def test_search_questions(self):
        res = self.client().post("/questions/search",
                                 json={"searchTerm": "title"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertEqual(data["total_questions"], 2)
        self.assertEqual(data["current_category"], "1")

    # test search quesitons api when search result 0 questions
    def test_search_questions_no_questions(self):
        res = self.client().post(
            "/questions/search", json={"searchTerm": "titdasdqwdsdasdqdsxcle"}
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["questions"], [])
        self.assertEqual(data["total_questions"], 0)
        self.assertEqual(data["current_category"], "1")

    # test get random but repeated questions to play quiz
    # using category 1 which has questions with id [20,21,22]
    def test_play_quiz(self):
        res = self.client().post(
            "/quizzes",
            json={
                "previous_questions": [20, 22],
                "quiz_category": {"type": "click", "id": 1},
            },
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"])

    # test questions finished  while play quiz
    def test_play_quiz_questions_finished(self):
        res = self.client().post(
            "/quizzes",
            json={
                "previous_questions": [20, 22, 21],
                "quiz_category": {"type": "click", "id": 1},
            },
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(
            data["question"], False
        )  # no questions availabe ,questions finished


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
