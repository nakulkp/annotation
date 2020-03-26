import flask
from flask import request, jsonify

from .articleSave import articleSave
from .login import login
from .markIrrelevant import markIrrelevant
from .markWithQuestion import markWithQuestion
from .review import review
from .userSignUp import userSignUp
from .articleContent import articleContent

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '<h1> HOME </h1>'

@app.route('/signup', methods=['POST'])
def api_signUp():
    requestParameters = request.args
    signUpStatus = userSignUp(requestParameters)
    return jsonify(signUpStatus)


@app.route('/login', methods=['POST'])
def api_login():
    requestParameters = request.args
    loginStatus = login(requestParameters)
    return jsonify(loginStatus)


@app.route('/articlecontent', methods=['GET'])
def api_articleContent():
    requestParameters = request.args
    resultList = articleContent(requestParameters)
    return jsonify(resultList)


@app.route('/markirrelevant', methods=['POST'])
def api_markIrrelevant():
    requestParameters = request.args
    markIrrelevant(requestParameters)


@app.route('/markquestion', methods=['GET'])
def api_markQuestion():
    requestParameters = request.args
    markWithQuestion(requestParameters)


@app.route('/articlesave', methods=['GET'])
def api_save():
    requestParameters = request.args
    articleSave(requestParameters)


@app.route('/articlereview', methods=['GET'])
def articleReview():
    requestParameters = request.args
    reviewValues = review(requestParameters)
    return reviewValues