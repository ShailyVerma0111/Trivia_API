import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    records = [records.format() for records in selection]
    current_records = records[start:end]

    return current_records

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.app_context().push()
    setup_db(app)

    #CORS(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,POST,DELETE"
        )
        return response

    @app.route("/categories")
    def retreive_categories():
        try: 
            categories = Category.query.order_by(Category.id).all()
            category_dic= {}  
    
            for category in categories:
                category_dic[category.id] = category.type

            return jsonify(
                {
                    "success": True,
                    "categories": category_dic,
                    "total_categories": len(Category.query.all()),
                }
            )
        except:
            abort(422)
    
    @app.route("/questions")
    def retreive_questions():
        try:        
            questions = Question.query.order_by(Question.id).all()
            categories = Category.query.order_by(Category.id).all()
            current_questions = paginate_questions(request, questions)
            current_category_dic = {}
            category_dic= {}  
    
            for category in categories:
                category_dic[category.id] = category.type

            for question in current_questions:
                current_category_dic[question['category']] = category_dic[question['category']]
            
            if len(current_questions) == 0:
                abort(404)

            return jsonify(
                {
                    "success": True,
                    "questions": current_questions,
                    "categories": category_dic,
                    "current_category": current_category_dic,
                    "total_questions": len(Question.query.all()),
                }
            )
        except:
            abort(422)
    
    
    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        try:    
            question = Question.query.filter(Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify(
                {
                    "success": True,
                    "deleted": question_id,
                    "current_questions": current_questions,
                    "total_questions": len(Question.query.all()),
                }
            )
        except:
            abort(422)


    @app.route("/questions", methods=["POST"])
    def create_question():
        body = request.get_json()

        new_question = body.get("question")
        new_answer = body.get("answer")
        new_difficulty = body.get("difficulty")
        new_category= body.get("category")

        try:
            question = Question(question=new_question,answer=new_answer,difficulty=new_difficulty,category=new_category)
            question.insert()

            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify(
                {
                    "success": True,
                    "created": question.id,
                    "current_questions": current_questions,
                    "total_questions": len(Question.query.all()),
                }
            )

        except:
            abort(422)


    @app.route("/search/questions", methods=["POST"])
    def search_question():
        body = request.get_json()
        search = body.get("searchTerm")

        try:
            selection = Question.query.order_by(Question.id).filter(
                    Question.question.ilike("%{}%".format(search))
                )
            current_questions = paginate_questions(request, selection)
            current_category_dic = {}
            for question in current_questions:
                category = Category.query.get(question['category'])
                current_category_dic[question['category']] = category.type

            return jsonify(
                {
                    "success": True,
                    "questions": current_questions,
                    "current_category": current_category_dic,
                    "total_questions": len(selection.all()),
                }
            )

        except:
            abort(422)

    @app.route("/categories/<int:category_id>/questions")
    def retreive_questions_by_category(category_id):
        try:
            questions = Question.query.filter(Question.category==category_id).order_by(Question.id).all()
            category = Category.query.get(category_id)
            current_questions = paginate_questions(request, questions)
            current_category_dic = {}  

            current_category_dic[category.id] = category.type

            if len(current_questions) == 0:
                abort(404)

            return jsonify(
                {
                    "success": True,
                    "questions": current_questions,
                    "current_category": current_category_dic,
                    "total_questions": len(questions),
                }
            )
        except:
            abort(422)

    @app.route("/quizzes", methods=["POST"])
    def retrieve_quize_questions():
        body = request.get_json()
        previous_question = body.get("previous_questions")
        quiz_category= body.get("quiz_category")
        random_question_dis = {}
    
        try:
            questions = Question.query.filter(Question.category==quiz_category['id']).all()            
            random_question = random.choice(questions)

            if len(previous_question)!=0:
                if previous_question == random_question.id:
                    random_question = random.choice(questions)

            random_question_dis['id'] = random_question.id
            random_question_dis['question'] = random_question.question
            random_question_dis['answer'] = random_question.answer
            random_question_dis['difficulty'] = random_question.difficulty
            random_question_dis['category'] = random_question.category        
        
            return jsonify(
                {
                    "success": True,
                    "question": random_question_dis,
                }
            )
        except:
            abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400
    
    @app.errorhandler(405)
    def method_not_allowed_request(error):
        return jsonify({"success": False, "error": 405, "message": "The method is not allowed for the requested URL."}), 405

    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({"success": False, "error": 500, "message": "internal server error"}), 500
    
    return app

