import flask
from flask import request, jsonify
from flask_cors import CORS

from adminDeleteCategory import adminDeleteCategory
from adminDeleteCommodity import adminDeleteCommodity
from adminDeleteDemand import adminDeleteDemand
from adminDeleteFactorValue import adminDeleteFactorValue
from adminDeleteMovingFactor import adminDeleteMovingFactor
from adminDeletePrice import adminDeletePrice
from adminDeleteRegion import adminDeleteRegion
from adminDeleteSCDisruption import adminDeleteSCDisruption
from adminDeleteSubCategory import adminDeleteSubCategory
from adminDeleteSupply import adminDeleteSupply
from articleContent import articleContent
from articleSave import articleSave
from markIrrelevant import markIrrelevant
from markWithQuestion import markWithQuestion
from review import review
from userSignUp import userSignUp
from login import login

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)


@app.route('/', methods=['POST'])
def home():
    data = request.get_json()
    # print(email)
    # print(data)
    return '<h1> HOME </h1>'


@app.route('/signup', methods=['POST'])
def api_signUp():
    requestParameters = request.get_json()
    signUpStatus = userSignUp(requestParameters)
    return jsonify(signUpStatus)


@app.route('/login', methods=['POST'])
def api_login():
    requestParameters = request.get_json()
    loginStatus = login(requestParameters)
    return jsonify(loginStatus)


@app.route('/articlecontent', methods=['GET'])
def api_articleContent():
    requestParameters = request.args
    resultList = articleContent(requestParameters)
    return jsonify(resultList)


@app.route('/markirrelevant', methods=['POST'])
def api_markIrrelevant():
    requestParameters = request.get_json()
    status = markIrrelevant(requestParameters)
    return jsonify(status)


@app.route('/markquestion', methods=['POST'])
def api_markQuestion():
    requestParameters = request.get_json()
    status = markWithQuestion(requestParameters)
    return jsonify(status)


@app.route('/articlesave', methods=['GET'])
def api_save():
    requestParameters = request.get_json()
    status = articleSave(requestParameters)
    return jsonify(status)


@app.route('/articlereview', methods=['GET'])
def articleReview():
    requestParameters = request.args
    reviewValues = review(requestParameters)
    return jsonify(reviewValues)


@app.route('/admindeletecategory', methods=['POST'])
def adminDeleteCategory():
    requestParameters = request.get_json()
    status = adminDeleteCategory(requestParameters)
    return jsonify(status)


@app.route('/admindeletecommodity', methods=['POST'])
def adminDeleteCommodity():
    requestParameters = request.get_json()
    status = adminDeleteCommodity(requestParameters)
    return jsonify(status)


@app.route('/admindeletedemand', methods=['POST'])
def adminDeleteDemand():
    requestParameters = request.get_json()
    status = adminDeleteDemand(requestParameters)
    return jsonify(status)


@app.route('/admindeletefactorvalue', methods=['POST'])
def adminDeleteFactorValue():
    requestParameters = request.get_json()
    status = adminDeleteFactorValue(requestParameters)
    return jsonify(status)

@app.route('/admindeletemovingfactor', methods=['POST'])
def adminDeleteMovingFactor():
    requestParameters = request.get_json()
    status = adminDeleteMovingFactor(requestParameters)
    return jsonify(status)

@app.route('/admindeleteprice', methods=['POST'])
def adminDeletePrice():
    requestParameters = request.get_json()
    status = adminDeletePrice(requestParameters)
    return jsonify(status)


@app.route('/admindeleteregion', methods=['POST'])
def adminDeleteRegion():
    requestParameters = request.get_json()
    status = adminDeleteRegion(requestParameters)
    return jsonify(status)

@app.route('/admindeletescdisruption', methods=['POST'])
def adminDeleteSCDisruption():
    requestParameters = request.get_json()
    status = adminDeleteSCDisruption(requestParameters)
    return jsonify(status)

@app.route('/admindeletesubcategory', methods=['POST'])
def adminDeleteSubCategory():
    requestParameters = request.get_json()
    status = adminDeleteSubCategory(requestParameters)
    return jsonify(status)

@app.route('/admindeletesupply', methods=['POST'])
def adminDeleteSupply():
    requestParameters = request.get_json()
    status = adminDeleteSupply(requestParameters)
    return jsonify(status)







@app.route('/upload', methods=['POST'])
def upload():
    requestParameters = request.args

    status = upload(requestParameters)
    return jsonify(status)
