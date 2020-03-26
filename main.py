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

    username = requestParameters["username"]
    email = requestParameters["email"]
    phone = requestParameters["phone"]
    password = requestParameters["password"]
    privilege = requestParameters["privilege"]
    if username or email or phone or password or privilege is None:
        return jsonify({'message': "Parameter Not Found"})

    signUpStatus = userSignUp(requestParameters)
    return jsonify(signUpStatus)


@app.route('/login', methods=['POST'])
def api_login():
    requestParameters = request.args

    email = requestParameters["email"]
    password = requestParameters["password"]
    if email or password is None:
        return jsonify({'message': "Parameter Not Found"})

    loginStatus = login(requestParameters)
    return jsonify(loginStatus)


@app.route('/articlecontent', methods=['GET'])
def api_articleContent():
    requestParameters = request.args

    user_id = requestParameters['user_id']
    flag = requestParameters['flag']
    if user_id or flag is None:
        return jsonify({'message': "Parameter Not Found"})

    resultList = articleContent(requestParameters)
    return jsonify(resultList)


@app.route('/markirrelevant', methods=['POST'])
def api_markIrrelevant():
    requestParameters = request.args

    article_id = requestParameters["article_id"]
    if article_id is None:
        return jsonify({'message': "Parameter Not Found"})

    status = markIrrelevant(requestParameters)
    return jsonify(status)


@app.route('/markquestion', methods=['GET'])
def api_markQuestion():
    requestParameters = request.args

    article_id = requestParameters["article_id"]
    question = requestParameters["question"]
    if article_id or question is None:
        return jsonify({'message': "Parameter Not Found"})

    status = markWithQuestion(requestParameters)
    return jsonify(status)


@app.route('/articlesave', methods=['GET'])
def api_save():
    requestParameters = request.args

    user_id = requestParameters['user_id']
    article_id = requestParameters['article_id']
    countries = requestParameters['countries']
    commodities = requestParameters['commodities']
    categories = requestParameters['categories']
    sub_categories = requestParameters['sub_categories']
    moving_factors = requestParameters['moving_factors']
    factor_value = requestParameters['factor_value']
    price_value = requestParameters['price_value']
    supply_value = requestParameters['supply_value']
    demand_value = requestParameters['demand_value']
    sc_disruption_value = requestParameters['sc_disruption_value']
    question = requestParameters['question']

    paramList = [user_id, article_id, countries, commodities, categories, sub_categories, moving_factors,
                 factor_value, price_value, supply_value, demand_value, sc_disruption_value, question]

    for param in paramList:
        if param is None:
            return jsonify({'message': "Parameter Not Found"})

    status = articleSave(requestParameters)
    return jsonify(status)


@app.route('/articlereview', methods=['GET'])
def articleReview():
    requestParameters = request.args

    user_id = requestParameters["user_id"]
    if user_id is None:
        return jsonify({'message': "Parameter Not Found"})

    status = review(requestParameters)
    return jsonify(status)
