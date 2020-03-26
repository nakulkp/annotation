import flask
from flask import request, jsonify
from flask_cors import CORS

from annotation.articleContent import articleContent
from annotation.articleSave import articleSave
from annotation.markIrrelevant import markIrrelevant
from annotation.markWithQuestion import markWithQuestion
from annotation.review import review
from annotation.userSignUp import userSignUp
from annotation.login import login
from annotation.adminDelete import adminDelete

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)


@app.route('/', methods=['POST'])
def home():
    data = request.get_json()
    #print(email)
    #print(data)
    return '<h1> HOME </h1>'


@app.route('/signup', methods=['POST'])
def api_signUp():
    requestParameters = request.get_json()

    username = requestParameters["username"]
    email = requestParameters["email"]
    phone = requestParameters["phone"]
    password = requestParameters["password"]
    privilege = requestParameters["privilege"]
    if (username or email or phone or password or privilege) is None:
        return jsonify({'message': "Parameter Not Found"})

    signUpStatus = userSignUp(requestParameters)
    #signUpStatus = "hi"
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


@app.route('/markquestion', methods=['POST'])
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
    country_id = requestParameters['country_id']
    commodity_id = requestParameters['commodity_id']
    category_id = requestParameters['category_id']
    subcategory_id = requestParameters['subcategory_id']
    moving_factor_id = requestParameters['moving_factor_id']
    factor_value_id = requestParameters['factor_value_id']
    price_value_id = requestParameters['price_value_id']
    supply_value_id = requestParameters['supply_value_id']
    demand_value_id = requestParameters['demand_value_id']
    sc_disruption_value_id = requestParameters['sc_disruption_value_id']
    question = requestParameters['question']

    paramList = [user_id, article_id, country_id, commodity_id, category_id, subcategory_id, moving_factor_id,
                 factor_value_id, price_value_id, supply_value_id, demand_value_id, sc_disruption_value_id, question]

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

    reviewValues = review(requestParameters)
    return jsonify(reviewValues)


@app.route('/admindelete', methods=['POST'])
def adminEditAdd():
    requestParameters = request.args

    user_id = requestParameters["user_id"]
    if user_id is None:
        return jsonify({'message': "Parameter Not Found"})

    status = adminDelete(requestParameters)
    return jsonify(status)


@app.route('/upload', methods=['POST'])
def upload():
    requestParameters = request.args

    status = upload(requestParameters)
    return jsonify(status)
