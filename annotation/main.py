import flask
from flask import request, jsonify
from flask_cors import CORS
import jwt
import datetime

from annotation.adminAddCategory import adminAddCategory
from annotation.adminAddCommodity import adminAddCommodity
from annotation.adminAddDemand import adminAddDemand
from annotation.adminAddFactorValue import adminAddFactorValue
from annotation.adminAddMovingFactor import adminAddMovingFactor
from annotation.adminAddPrice import adminAddPrice
from annotation.adminAddRegion import adminAddRegion
from annotation.adminAddSCDisruption import adminAddSCDisruption
from annotation.adminAddSubCategory import adminAddSubCategory
from annotation.adminAddSupply import adminAddSupply
from annotation.adminDeleteCategory import adminDeleteCategory
from annotation.adminDeleteCommodity import adminDeleteCommodity
from annotation.adminDeleteDemand import adminDeleteDemand
from annotation.adminDeleteFactorValue import adminDeleteFactorValue
from annotation.adminDeleteMovingFactor import adminDeleteMovingFactor
from annotation.adminDeletePrice import adminDeletePrice
from annotation.adminDeleteRegion import adminDeleteRegion
from annotation.adminDeleteSCDisruption import adminDeleteSCDisruption
from annotation.adminDeleteSubCategory import adminDeleteSubCategory
from annotation.adminDeleteSupply import adminDeleteSupply
from annotation.adminUsersFetch import adminUsersFetch
from annotation.articleContent import articleContent
from annotation.articleSave import articleSave
from annotation.csvUpload import csvUpload
from annotation.fetchCategory import fetchCategory
from annotation.fetchCommodity import fetchCommodity
from annotation.fetchDemand import fetchDemand
from annotation.fetchFactorValue import fetchFactorValue
from annotation.fetchMovingFactor import fetchMovingFactor
from annotation.fetchPrice import fetchPrice
from annotation.fetchRegion import fetchRegion
from annotation.fetchSCDisruption import fetchSCDisruption
from annotation.fetchSubCategory import fetchSubCategory
from annotation.fetchSupply import fetchSupply
from annotation.markIrrelevant import markIrrelevant
from annotation.markWithQuestion import markWithQuestion
from annotation.review import review
from annotation.userSignUp import userSignUp
from annotation.login import login

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "!5@adjh@#!@QSQsw1!@c"
cors = CORS(app)


@app.route('/', methods=['POST'])
def api_home():
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
    email = requestParameters['email']
    authenticated = loginStatus.pop()
    if authenticated['auth'] == 'success':
        token = jwt.encode(
            {'email': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config["SECRET_KEY"])
        return jsonify({'token': token.decode('UTF-8')}, loginStatus)
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


@app.route('/articlesave', methods=['POST'])
def api_save():
    requestParameters = request.get_json()
    status = articleSave(requestParameters)
    return jsonify(status)


@app.route('/articlereview', methods=['GET'])
def api_articleReview():
    requestParameters = request.args
    reviewValues = review(requestParameters)
    return jsonify(reviewValues)


@app.route('/admindeletecategory', methods=['POST'])
def api_adminDeleteCategory():
    requestParameters = request.get_json()
    status = adminDeleteCategory(requestParameters)
    return jsonify(status)


@app.route('/admindeletecommodity', methods=['POST'])
def api_adminDeleteCommodity():
    requestParameters = request.get_json()
    status = adminDeleteCommodity(requestParameters)
    return jsonify(status)


@app.route('/admindeletedemand', methods=['POST'])
def api_adminDeleteDemand():
    requestParameters = request.get_json()
    status = adminDeleteDemand(requestParameters)
    return jsonify(status)


@app.route('/admindeletefactorvalue', methods=['POST'])
def api_adminDeleteFactorValue():
    requestParameters = request.get_json()
    status = adminDeleteFactorValue(requestParameters)
    return jsonify(status)


@app.route('/admindeletemovingfactor', methods=['POST'])
def api_adminDeleteMovingFactor():
    requestParameters = request.get_json()
    status = adminDeleteMovingFactor(requestParameters)
    return jsonify(status)


@app.route('/admindeleteprice', methods=['POST'])
def api_adminDeletePrice():
    requestParameters = request.get_json()
    status = adminDeletePrice(requestParameters)
    return jsonify(status)


@app.route('/admindeleteregion', methods=['POST'])
def api_adminDeleteRegion():
    requestParameters = request.get_json()
    status = adminDeleteRegion(requestParameters)
    return jsonify(status)


@app.route('/admindeletescdisruption', methods=['POST'])
def api_adminDeleteSCDisruption():
    requestParameters = request.get_json()
    status = adminDeleteSCDisruption(requestParameters)
    return jsonify(status)


@app.route('/admindeletesubcategory', methods=['POST'])
def api_adminDeleteSubCategory():
    requestParameters = request.get_json()
    status = adminDeleteSubCategory(requestParameters)
    return jsonify(status)


@app.route('/admindeletesupply', methods=['POST'])
def api_adminDeleteSupply():
    requestParameters = request.get_json()
    status = adminDeleteSupply(requestParameters)
    return jsonify(status)


@app.route('/adminaddcategory', methods=['POST'])
def api_adminAddCategory():
    requestParameters = request.get_json()
    status = adminAddCategory(requestParameters)
    return jsonify(status)


@app.route('/adminaddcommodity', methods=['POST'])
def api_adminAddCommodity():
    requestParameters = request.get_json()
    status = adminAddCommodity(requestParameters)
    return jsonify(status)


@app.route('/adminaddDemand', methods=['POST'])
def api_adminAddDemand():
    requestParameters = request.get_json()
    status = adminAddDemand(requestParameters)
    return jsonify(status)


@app.route('/adminaddfactorvalue', methods=['POST'])
def api_adminAddFactorValue():
    requestParameters = request.get_json()
    status = adminAddFactorValue(requestParameters)
    return jsonify(status)


@app.route('/adminaddmovingfactor', methods=['POST'])
def api_adminAddMovingFactor():
    requestParameters = request.get_json()
    status = adminAddMovingFactor(requestParameters)
    return jsonify(status)


@app.route('/adminaddprice', methods=['POST'])
def api_adminAddPrice():
    requestParameters = request.get_json()
    status = adminAddPrice(requestParameters)
    return jsonify(status)


@app.route('/adminaddregion', methods=['POST'])
def api_adminAddRegion():
    requestParameters = request.get_json()
    status = adminAddRegion(requestParameters)
    return jsonify(status)


@app.route('/adminaddscdisruption', methods=['POST'])
def api_adminAddSCDisruption():
    requestParameters = request.get_json()
    status = adminAddSCDisruption(requestParameters)
    return jsonify(status)


@app.route('/adminaddsubcategory', methods=['POST'])
def api_adminAddSubCategory():
    requestParameters = request.get_json()
    status = adminAddSubCategory(requestParameters)
    return jsonify(status)


@app.route('/adminaddsupply', methods=['POST'])
def api_adminAddSupply():
    requestParameters = request.get_json()
    status = adminAddSupply(requestParameters)
    return jsonify(status)


@app.route('/fetchcategory', methods=['GET'])
def api_fetchCategory():
    valueList = fetchCategory()
    return jsonify(valueList)


@app.route('/fetchcommodity', methods=['GET'])
def api_fetchCommodity():
    valueList = fetchCommodity()
    return jsonify(valueList)


@app.route('/fetchdemand', methods=['GET'])
def api_fetchDemand():
    valueList = fetchDemand()
    return jsonify(valueList)


@app.route('/fetchfactorvalue', methods=['GET'])
def api_fetchFactorValue():
    valueList = fetchFactorValue()
    return jsonify(valueList)


@app.route('/fetchmovingfactor', methods=['GET'])
def api_fetchMovingFactor():
    valueList = fetchMovingFactor()
    return jsonify(valueList)


@app.route('/fetchprice', methods=['GET'])
def api_fetchPrice():
    valueList = fetchPrice()
    return jsonify(valueList)


@app.route('/fetchregion', methods=['GET'])
def api_fetchRegion():
    valueList = fetchRegion()
    return jsonify(valueList)


@app.route('/fetchscdisruption', methods=['GET'])
def api_fetchSCDisruption():
    valueList = fetchSCDisruption()
    return jsonify(valueList)


@app.route('/fetchsubcategory', methods=['GET'])
def api_fetchSubCategory():
    valueList = fetchSubCategory()
    return jsonify(valueList)


@app.route('/fetchsupply', methods=['GET'])
def api_fetchSupply():
    valueList = fetchSupply()
    return jsonify(valueList)


@app.route('/csvupload', methods=['POST'])
def api_csvUpload():
    requestParameters = request.get_json()
    status = csvUpload(requestParameters)
    return jsonify(status)


@app.route('/adminusersfetch', methods=['GET'])
def api_adminUsersFetch():
    #requestParameters = request.get_json()
    status = adminUsersFetch()
    return jsonify(status)

