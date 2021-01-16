
## Trivia App:

-trivia app the place where you can play and gain information about different fileds and categories
-in trivia you can post questions ,Delete questions ,get answers of all questions if you want and play excited quizzes in the category you want to
-what are you  waiting for ? just click play and start enjoy a great game and great knowledge 


## Getting Started:

-this project not hosted yet you can run it locally on your machine
-all you need to get start with frontend server you can find on ./frontend/README.md
-all you need to get start with backend server you can find on ./backend/README.md
-in README.md of frontend and backend you will find all depencies and commands to run the server and test it 
-all prerequests you find in README.md files

## Api Refrence

   ## Get started with api refrence
   -Base url: at present this app run locally at http:localhost/5000
   -Authentication:this version of the app does not require authentication or API keys
   
   ## Error handling 
   -errors return json object in format {"success":False,"error":404,"message":"not found"}
   -the app will return three types of errors:
     1. bad request (400)
     2. not found (404)
     3. unporcessable (422)
     
   ## End points Library
		     
		Endpoints
		GET '/categories'
		GET '/questions'
		POST '/questions'
		DELETE '/questions/id'
		GET '/categories/category_id/questions'
		POST '/questions/search'
		POST '/quizzes'


		########################################################################

		GET '/categories'
		- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the 
		 category
		- Request Arguments: None
		- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.
		{'1' : "Science",
		'2' : "Art",
		'3' : "Geography",
		'4' : "History",
		'5' : "Entertainment",
		'6' : "Sports"}

		```#########################################################################

		GET '/question'

		-Fetch a number of questions depend on page numer and questions/page value
		-Request Arguments: Page number as query parameter in url
		-Returns: Object has questions,total number of questions,categories,current_category
		-Sample Request: 'curl http//localhost/3000/questions?page=2'
		{'success':True,
		'questions':[{question1},{question2},...],
		'total_questions':19,
		'categories':{'1' : "Science",'2' : "Art",'3' : "Geography",'4' : "History",'5' : "Entertainment"},
		'current_category':'Art'
		}

		#########################################################################

		DELETE '/question/id'

		-Delete question with given id number
		-Request Argument: question id passed as query parameter in url
		-response: json object with success state
		-Sample Request: `curl -X DELETE http:localhost:3000/questions/2`
		{'success':True }

		#########################################################################

		POST '/questions'

		-Create new question and added to database
		-Request: json object contain question,answer,difficulty and category
		-Response: json object contain success state,new question id
		-Sample Request: `curl -X POST http:localhost:3000/questions' -d "{"question":"what
		is","answer":"me","difficulty":"2","category":"3"}"`
		     
		{"success":True,"question_id":25}

		########################################################################

		GET '/categories/category_id/questions

		-get questions of specific category
		-Request Arguments:None
		-Response:return json object contain questions of the category,total number of questions and current category id
		-sample `curl http://localhost/3000/categories/2/questions`
		{
		    "questions":[{question1},{question2},....],
		    "total_questions":4,
		    "current_category":"2"
		}

		```############################################################33

		POST "/questions/search"

		-Search in questions using searchTerm as substring of question
		-Request Arguments: json object contain searchTerm only
		-Response:json object contain questions,number of questions,current category
		-sample `curl -X POST http://localhost:3000/questions/search -d "{"searchTerm":"title"}" `
		{
		"questions":[{question1},{question2},....],
		"total_questions":2,
		"current_category":"1",
		"success":True
		}

		```#############################################################################################

		POST '/quizzes'
		-get questions to start play the quiz for all questions or questions of selected category
		-Request Argument: json object contain previous questions and quiz category selected
		-Response: json object contain question which is not one of the previous questions and from the same category and 
		 scuccess state
		-Sample Request: ``curl -X POST http://localhost:3000/quizzes -d "{
				"previous_questions": [20, 22],
				"quiz_category": {"type": "click", "id": 1},}" ``

		{'answer': 'Alexander Fleming', 'category': 1, 'question': 'Who discovered penicillin?', 'id': 21, 'difficulty': 3}
		
		
## Authors

-udacity fullstack nano degree program team
-Eslam Zaki (solomzaki840@gmail.com)


## Acknowledgments

-this project was udacity project for a program and as a student in the program my rule was write Rest APIs of the backend and write test APIs and error handling
		
		
		
		


		   
		     





