# API Development and Documentation Final Project

## Trivia App

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the project repository and [clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The [backend](./backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

> View the [Backend README](./backend/README.md) for more details.

### Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads?

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API.

> View the [Frontend README](./frontend/README.md) for more details.

## Getting Started

### Pre-requisites and Local Development 
Developers using this project should already have Python3, pip and node installed on their local machines.

#### Backend

From the backend folder run `pip install requirements.txt`. All required packages are included in the requirements file.
Before running the app setup your loacl trivia db.

To setup trivia db:
```
createdb trivia
psql trivia < trivia.psql
```

To run the application run the following commands: 
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration. 

#### Frontend

From the frontend folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
npm start 
```

By default, the frontend will run on localhost:3000. 

### Tests
In order to run tests navigate to the backend folder and run the following commands: 

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

The first time you run the tests, omit the dropdb command. 

All tests are kept in that file and should be maintained as updates are made to app functionality.

## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 
- 500: Internal server error

### Endpoints 
#### GET /categories
- General:
    - Returns a list of category objects, success value, and total number of categories 
- Sample: `curl http://127.0.0.1:5000/categories`

``` 
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true,
  "total_categories": 6
}
```

#### GET /questions
- General:
    - Returns a list of questions objects, success value,categories, current categories and total number of questions
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1. 
- Sample: `curl http://127.0.0.1:5000/questions`

``` 
{
   "categories":{
      "1":"Science",
      "2":"Art",
      "3":"Geography",
      "4":"History",
      "5":"Entertainment",
      "6":"Sports"
   },
   "current_category":{
      "2":"Art",
      "3":"Geography",
      "4":"History",
      "5":"Entertainment",
      "6":"Sports"
   },
   "questions":[
      {
         "answer":"Apollo 13",
         "category":5,
         "difficulty":4,
         "id":2,
         "question":"What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
      },
      {
         "answer":"Tom Cruise",
         "category":5,
         "difficulty":4,
         "id":4,
         "question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
      },
      {
         "answer":"Maya Angelou",
         "category":4,
         "difficulty":2,
         "id":5,
         "question":"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
         "answer":"Edward Scissorhands",
         "category":5,
         "difficulty":3,
         "id":6,
         "question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
      },
      {
         "answer":"Muhammad Ali",
         "category":4,
         "difficulty":1,
         "id":9,
         "question":"What boxer's original name is Cassius Clay?"
      },
      {
         "answer":"Brazil",
         "category":6,
         "difficulty":3,
         "id":10,
         "question":"Which is the only team to play in every soccer World Cup tournament?"
      },
      {
         "answer":"Uruguay",
         "category":6,
         "difficulty":4,
         "id":11,
         "question":"Which country won the first ever soccer World Cup in 1930?"
      },
      {
         "answer":"The Palace of Versailles",
         "category":3,
         "difficulty":3,
         "id":14,
         "question":"In which royal palace would you find the Hall of Mirrors?"
      },
      {
         "answer":"Agra",
         "category":3,
         "difficulty":2,
         "id":15,
         "question":"The Taj Mahal is located in which Indian city?"
      },
      {
         "answer":"Escher",
         "category":2,
         "difficulty":1,
         "id":16,
         "question":"Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
      }
   ],
   "success":true,
   "total_questions":18
}
```

#### GET /categories/<int:category_id>/questions
- General:
    - Returns a list of questions objects, success value,current categories and total number of questions
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1. 
- Sample: `curl http://127.0.0.1:5000/categories/3/questions`

``` 
{
   "current_category":{
      "3":"Geography"
   },
   "questions":[
      {
         "answer":"The Palace of Versailles",
         "category":3,
         "difficulty":3,
         "id":14,
         "question":"In which royal palace would you find the Hall of Mirrors?"
      },
      {
         "answer":"Agra",
         "category":3,
         "difficulty":2,
         "id":15,
         "question":"The Taj Mahal is located in which Indian city?"
      },
      {
         "answer":"Lake Victoria ",
         "category":3,
         "difficulty":2,
         "id":25,
         "question":"What is the largest lake in Africa? "
      }
   ],
   "success":true,
   "total_questions":3
}
```
#### POST /questions
- General:
    - Creates a new question using the submitted question, answer, difficulty and category. Returns the id of the     created question, success value, total questions, and question list based on current page number to update the frontend. 
- `curl -X POST -H "Content-Type: application/json" -d '{"question": "What is the largest lake in Africa? ", "answer": "Lake Victoria ", "difficulty": 2, "category": 3}' http://127.0.0.1:5000/questions`
```
{
   "created":26,
   "current_questions":[
      {
         "answer":"Apollo 13",
         "category":5,
         "difficulty":4,
         "id":2,
         "question":"What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
      },
      {
         "answer":"Tom Cruise",
         "category":5,
         "difficulty":4,
         "id":4,
         "question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
      },
      {
         "answer":"Maya Angelou",
         "category":4,
         "difficulty":2,
         "id":5,
         "question":"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
         "answer":"Edward Scissorhands",
         "category":5,
         "difficulty":3,
         "id":6,
         "question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
      },
      {
         "answer":"Muhammad Ali",
         "category":4,
         "difficulty":1,
         "id":9,
         "question":"What boxer's original name is Cassius Clay?"
      },
      {
         "answer":"Brazil",
         "category":6,
         "difficulty":3,
         "id":10,
         "question":"Which is the only team to play in every soccer World Cup tournament?"
      },
      {
         "answer":"Uruguay",
         "category":6,
         "difficulty":4,
         "id":11,
         "question":"Which country won the first ever soccer World Cup in 1930?"
      },
      {
         "answer":"The Palace of Versailles",
         "category":3,
         "difficulty":3,
         "id":14,
         "question":"In which royal palace would you find the Hall of Mirrors?"
      },
      {
         "answer":"Agra",
         "category":3,
         "difficulty":2,
         "id":15,
         "question":"The Taj Mahal is located in which Indian city?"
      },
      {
         "answer":"Escher",
         "category":2,
         "difficulty":1,
         "id":16,
         "question":"Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
      }
   ],
   "success":true,
   "total_questions":19
}
```
#### POST /search/questions
- General:
    - Search question using the submitted searchTerm. Returns the current category, success value, total questions, and matching question list based on current page number to update the frontend.
- `curl -X POST -H "Content-Type: application/json" -d '{"searchTerm": "auto"}' http://127.0.0.1:5000/search/questions`
```
{
   "current_category":{
      "4":"History"
   },
   "questions":[
      {
         "answer":"Maya Angelou",
         "category":4,
         "difficulty":2,
         "id":5,
         "question":"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      }
   ],
   "success":true,
   "total_questions":1
}
```
#### POST /quizzes
- General:
    - Retrive random question for quize based on submitted category details, also accepts previousquestion as request parameter to make sure the quize question is not same as previous question. Returns the quetion and success value.
- `curl -X POST -H "Content-Type: application/json" -d '{"previous_questions": [],"quiz_category": {"type": "Science","id": "1"}}' http://127.0.0.1:5000/quizzes`

```
{
   "question":{
      "answer":"The Liver",
      "category":1,
      "difficulty":4,
      "id":20,
      "question":"What is the heaviest organ in the human body?"
   },
   "success":true
}
```

#### DELETE /questions/<int:question_id>
- General:
    - Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value, total questions, and question list based on current page number to update the frontend. 
- `curl -X DELETE http://127.0.0.1:5000/questions/23`
```
{
   "current_questions":[
      {
         "answer":"Apollo 13",
         "category":5,
         "difficulty":4,
         "id":2,
         "question":"What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
      },
      {
         "answer":"Tom Cruise",
         "category":5,
         "difficulty":4,
         "id":4,
         "question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
      },
      {
         "answer":"Maya Angelou",
         "category":4,
         "difficulty":2,
         "id":5,
         "question":"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
         "answer":"Edward Scissorhands",
         "category":5,
         "difficulty":3,
         "id":6,
         "question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
      },
      {
         "answer":"Muhammad Ali",
         "category":4,
         "difficulty":1,
         "id":9,
         "question":"What boxer's original name is Cassius Clay?"
      },
      {
         "answer":"Brazil",
         "category":6,
         "difficulty":3,
         "id":10,
         "question":"Which is the only team to play in every soccer World Cup tournament?"
      },
      {
         "answer":"Uruguay",
         "category":6,
         "difficulty":4,
         "id":11,
         "question":"Which country won the first ever soccer World Cup in 1930?"
      },
      {
         "answer":"The Palace of Versailles",
         "category":3,
         "difficulty":3,
         "id":14,
         "question":"In which royal palace would you find the Hall of Mirrors?"
      },
      {
         "answer":"Agra",
         "category":3,
         "difficulty":2,
         "id":15,
         "question":"The Taj Mahal is located in which Indian city?"
      },
      {
         "answer":"Escher",
         "category":2,
         "difficulty":1,
         "id":16,
         "question":"Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
      }
   ],
   "deleted":23,
   "success":true,
   "total_questions":18
}
```
## Deployment N/A

## Acknowledgements 
Had great fun developing this project, thanks to whole team of udacity for amazing course! 
