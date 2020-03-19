import flask
from flask import request, jsonify
from login import login
from userSignUp import userSignUp
from articleContent import articleContent

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '<h1> HOME </h1>'


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Requested Resource Not Found!!!</p>", 404


@app.route('/signup', methods=['GET'])
def api_signUp():
    requestParameters = request.args
    signUpStatus = userSignUp(requestParameters)
    return jsonify(signUpStatus)


@app.route('/login', methods=['GET'])
def api_login():
    requestParameters = request.args
    loginStatus = login(requestParameters)
    return jsonify(loginStatus)


@app.route('/articlecontent', methods=['GET'])
def api_articleContent():
    requestParameters = request.args  # takes args from request
    resultList = articleContent(requestParameters)
    return jsonify(resultList)


app.run()
