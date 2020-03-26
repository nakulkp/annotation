import flask
from flask import request, jsonify

from annotation.articleContent import articleContent
from annotation.articleSave import articleSave
from annotation.markIrrelevant import markIrrelevant
from annotation.markWithQuestion import markWithQuestion
from annotation.review import review
from annotation.userSignUp import userSignUp
from annotation.login import login


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
    status =  markIrrelevant(requestParameters)
    return jsonify(status)

@app.route('/markquestion', methods=['GET'])
def api_markQuestion():
    requestParameters = request.args
    status =  markWithQuestion(requestParameters)
    return jsonify(status)


@app.route('/articlesave', methods=['GET'])
def api_save():
    requestParameters = request.args
    status =  articleSave(requestParameters)
    return jsonify(status)

@app.route('/articlereview', methods=['GET'])
def articleReview():
    requestParameters = request.args
    status = review(requestParameters)
    return jsonify(status)
