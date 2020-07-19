import flask
from flask import request, jsonify, Response
from flask import make_response
from flask_cors import CORS
import jwt
import datetime

from functools import wraps

from annotation.adminAddCommodity import adminAddCommodity
from annotation.adminAddDemand import adminAddDemand
from annotation.adminAddFactor import adminAddFactor
from annotation.adminAddPrice import adminAddPrice
from annotation.adminAddSubFactor import adminAddSubFactor
from annotation.adminAddSubFactorValue import adminAddSubFactorValue
from annotation.adminAddSupply import adminAddSupply
from annotation.adminAddCommodityDescription import adminAddCommodityDescription
from annotation.adminAddRegionOfEvent import adminAddRegionofEvent

from annotation.adminDeleteCommodity import adminDeleteCommodity
from annotation.adminDeleteCommodityDescription import adminDeleteCommodityDescription
from annotation.adminDeleteDemand import adminDeleteDemand
from annotation.adminDeleteFactor import adminDeleteFactor
from annotation.adminDeletePrice import adminDeletePrice
from annotation.adminDeleteRegionOfEvent import adminDeleteRegionOfEvent
from annotation.adminDeleteRegionOfImpact import adminDeleteRegionOfImpact
from annotation.adminDeleteSubFactor import adminDeleteSubFactor
from annotation.adminDeleteSubFactorValue import adminDeleteSubFactorValue
from annotation.adminDeleteSupply import adminDeleteSupply

from annotation.adminUserEdit import adminUserEdit
from annotation.adminUsersFetch import adminUsersFetch

from annotation.annotationCount import annotationCount
from annotation.articleContent import articleContent
from annotation.articleContentId import articleContentId
from annotation.articleContentNav import articleContentNav
from annotation.articleCount import articleCount
from annotation.articleSave import articleSave

from annotation.csvUpload import csvUpload

from annotation.deleteMapping import deleteMapping

from annotation.fetchCategory import fetchCategory
from annotation.fetchCommodity import fetchCommodity
from annotation.fetchDemand import fetchDemand
from annotation.fetchFactorValue import fetchFactorValue
from annotation.fetchMapping import fetchMapping
from annotation.fetchMovingFactor import fetchMovingFactor
from annotation.fetchPrice import fetchPrice
from annotation.fetchRegion import fetchRegion
from annotation.fetchSubCategory import fetchSubCategory
from annotation.fetchSupply import fetchSupply
from annotation.fetchUsers import fetchUsers

from annotation.markIrrelevant import markIrrelevant
from annotation.markWithQuestion import markWithQuestion
from annotation.review import review
from annotation.updateMapping import updateMapping
from annotation.userSignUp import userSignUp
from annotation.login import login
from annotation.exportCsv import exportCsv
from annotation.movingFactorConstraints import movingFactorConstraints
from annotation.subCategoryConstraints import subCategoryConstraints

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "!5@adjh@#!@QSQsw1!@c"
app.config["SALT"] = "3@v2p#nc@asD!@$D%42a5%^Aa6AGU&Y"
cors = CORS(app)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        requestParameters = request.get_json()
        token = requestParameters["token"]
        if not token:
            return jsonify({'message': 'token missing'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Invalid Token'}), 403
        return f(*args, **kwargs)

    return decorated


@app.route('/', methods=['POST'])
def api_home():
    return jsonify("Home")


@app.route('/signup', methods=['POST'])
# @token_required
def api_signUp():
    requestParameters = request.get_json()
    signUpStatus = userSignUp(requestParameters)
    return jsonify(signUpStatus)


@app.route('/login', methods=['POST'])
def api_login():
    requestParameters = request.get_json()
    loginStatus = login(requestParameters)
    email = requestParameters['email']
    if loginStatus['auth'] == 'success':
        token = jwt.encode(
            {'email': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)},
            app.config["SECRET_KEY"])
        return jsonify({'token': token.decode('UTF-8')}, loginStatus)
    return jsonify(loginStatus)


@app.route('/articlecontent', methods=['POST'])
@token_required
def api_articleContent():
    requestParameters = request.get_json()
    resultList = articleContent(requestParameters)
    return jsonify(resultList)


@app.route('/articlecontentid', methods=['POST'])
@token_required
def api_articleContentId():
    requestParameters = request.get_json()
    resultList = articleContentId(requestParameters)
    return jsonify(resultList)


@app.route('/articlecontentnav', methods=['POST'])
@token_required
def api_articleContentNav():
    requestParameters = request.get_json()
    resultList = articleContentNav(requestParameters)
    return jsonify(resultList)


@app.route('/articlecount', methods=['POST'])
@token_required
def api_articleCount():
    requestParameters = request.get_json()
    resultList = articleCount(requestParameters)
    return jsonify(resultList)


@app.route('/markirrelevant', methods=['POST'])
@token_required
def api_markIrrelevant():
    requestParameters = request.get_json()
    status = markIrrelevant(requestParameters)
    return jsonify(status)


@app.route('/markquestion', methods=['POST'])
@token_required
def api_markQuestion():
    requestParameters = request.get_json()
    status = markWithQuestion(requestParameters)
    return jsonify(status)


@app.route('/articlesave', methods=['POST'])
@token_required
def api_save():
    requestParameters = request.get_json()
    status = articleSave(requestParameters)
    return jsonify(status)


@app.route('/articlereview', methods=['POST'])
@token_required
def api_articleReview():
    requestParameters = request.get_json()
    reviewValues = review(requestParameters)
    return jsonify(reviewValues)


@app.route('/admindeletecommodity', methods=['POST'])
@token_required
def api_adminDeleteCommodity():
    requestParameters = request.get_json()
    status = adminDeleteCommodity(requestParameters)
    return jsonify(status)


@app.route('/admindeletecommoditydescriptiom', methods=['POST'])
@token_required
def api_adminDeleteCommodityDescription():
    requestParameters = request.get_json()
    status = adminDeleteCommodityDescription(requestParameters)
    return jsonify(status)

@app.route('/admindeleteregionofevent', methods=['POST'])
@token_required
def api_adminDeleteRegionOfEvent():
    requestParameters = request.get_json()
    status = adminDeleteRegionOfEvent(requestParameters)
    return jsonify(status)

@app.route('/admindeleteregionofimpact', methods=['POST'])
@token_required
def api_adminDeleteRegionOfImpact():
    requestParameters = request.get_json()
    status = adminDeleteRegionOfImpact(requestParameters)
    return jsonify(status)

@app.route('/admindeletefactor', methods=['POST'])
@token_required
def api_adminDeleteFactor():
    requestParameters = request.get_json()
    status = adminDeleteFactor(requestParameters)
    return jsonify(status)

@app.route('/admindeletesubfactor', methods=['POST'])
@token_required
def api_adminDeleteSubFactor():
    requestParameters = request.get_json()
    status = adminDeleteSubFactor(requestParameters)
    return jsonify(status)

@app.route('/admindeletesubfactorvalue', methods=['POST'])
@token_required
def api_adminDeleteSubFactorValue():
    requestParameters = request.get_json()
    status = adminDeleteSubFactorValue(requestParameters)
    return jsonify(status)

@app.route('/admindeletedemand', methods=['POST'])
@token_required
def api_adminDeleteDemand():
    requestParameters = request.get_json()
    status = adminDeleteDemand(requestParameters)
    return jsonify(status)


@app.route('/admindeleteprice', methods=['POST'])
@token_required
def api_adminDeletePrice():
    requestParameters = request.get_json()
    status = adminDeletePrice(requestParameters)
    return jsonify(status)


@app.route('/admindeletesupply', methods=['POST'])
@token_required
def api_adminDeleteSupply():
    requestParameters = request.get_json()
    status = adminDeleteSupply(requestParameters)
    return jsonify(status)


@app.route('/adminaddcommoditydescription', methods=['POST'])
@token_required
def api_adminAddCommodityDescription():
    requestParameters = request.get_json()
    status = adminAddCommodityDescription(requestParameters)
    return jsonify(status)


@app.route('/adminaddcommodity', methods=['POST'])
@token_required
def api_adminAddCommodity():
    requestParameters = request.get_json()
    status = adminAddCommodity(requestParameters)
    return jsonify(status)


@app.route('/adminaddDemand', methods=['POST'])
@token_required
def api_adminAddDemand():
    requestParameters = request.get_json()
    status = adminAddDemand(requestParameters)
    return jsonify(status)


@app.route('/adminaddprice', methods=['POST'])
@token_required
def api_adminAddPrice():
    requestParameters = request.get_json()
    status = adminAddPrice(requestParameters)
    return jsonify(status)


@app.route('/adminaddregionofevent', methods=['POST'])
@token_required
def api_adminAddRegionofEvent():
    requestParameters = request.get_json()
    status = adminAddRegionofEvent(requestParameters)
    return jsonify(status)


@app.route('/adminaddsupply', methods=['POST'])
@token_required
def api_adminAddSupply():
    requestParameters = request.get_json()
    status = adminAddSupply(requestParameters)
    return jsonify(status)


@app.route('/adminaddfactor', methods=['POST'])
@token_required
def api_adminAddFactor():
    requestParameters = request.get_json()
    status = adminAddFactor(requestParameters)
    return jsonify(status)


@app.route('/adminaddsubfactor', methods=['POST'])
@token_required
def api_adminAddSubFactor():
    requestParameters = request.get_json()
    status = adminAddSubFactor(requestParameters)
    return jsonify(status)


@app.route('/adminaddsubfactorvalue', methods=['POST'])
@token_required
def api_adminAddSubFactorValue():
    requestParameters = request.get_json()
    status = adminAddSubFactorValue(requestParameters)
    return jsonify(status)


@app.route('/fetchcategory', methods=['POST'])
@token_required
def api_fetchCategory():
    requestParameters = request.get_json()
    valueList = fetchCategory(requestParameters)
    return jsonify(valueList)


@app.route('/fetchcommodity', methods=['POST'])
@token_required
def api_fetchCommodity():
    requestParameters = request.get_json()
    valueList = fetchCommodity(requestParameters)
    return jsonify(valueList)


@app.route('/fetchdemand', methods=['POST'])
@token_required
def api_fetchDemand():
    requestParameters = request.get_json()
    valueList = fetchDemand(requestParameters)
    return jsonify(valueList)


@app.route('/fetchfactorvalue', methods=['POST'])
@token_required
def api_fetchFactorValue():
    requestParameters = request.get_json()
    valueList = fetchFactorValue(requestParameters)
    return jsonify(valueList)


@app.route('/fetchmapping', methods=['POST'])
@token_required
def api_fetchMapping():
    requestParameters = request.get_json()
    valueList = fetchMapping(requestParameters)
    return jsonify(valueList)


@app.route('/fetchmovingfactor', methods=['POST'])
@token_required
def api_fetchMovingFactor():
    requestParameters = request.get_json()
    valueList = fetchMovingFactor(requestParameters)
    return jsonify(valueList)


@app.route('/fetchprice', methods=['POST'])
@token_required
def api_fetchPrice():
    requestParameters = request.get_json()
    valueList = fetchPrice(requestParameters)
    return jsonify(valueList)


@app.route('/fetchregion', methods=['POST'])
@token_required
def api_fetchRegion():
    requestParameters = request.get_json()
    valueList = fetchRegion(requestParameters)
    return jsonify(valueList)


@app.route('/fetchsubcategory', methods=['POST'])
@token_required
def api_fetchSubCategory():
    requestParameters = request.get_json()
    valueList = fetchSubCategory(requestParameters)
    return jsonify(valueList)


@app.route('/fetchsupply', methods=['POST'])
@token_required
def api_fetchSupply():
    requestParameters = request.get_json()
    valueList = fetchSupply(requestParameters)
    return jsonify(valueList)


@app.route('/fetchusers', methods=['POST'])
@token_required
def api_fetchUsers():
    requestParameters = request.get_json()
    valueList = fetchUsers(requestParameters)
    return jsonify(valueList)


@app.route('/csvupload', methods=['POST'])
def api_csvUpload():
    requestParameters = request.get_json()
    status = csvUpload(requestParameters)
    return jsonify(status)


@app.route('/deletemapping', methods=['POST'])
def api_deleteMapping():
    requestParameters = request.get_json()
    status = deleteMapping(requestParameters)
    return jsonify(status)


@app.route('/adminusersfetch', methods=['POST'])
@token_required
def api_adminUsersFetch():
    requestParameters = request.get_json()
    valuesList = adminUsersFetch(requestParameters)
    return jsonify(valuesList)


@app.route('/adminuseredit', methods=['POST'])
@token_required
def api_adminUsersEdit():
    requestParameters = request.get_json()
    status = adminUserEdit(requestParameters)
    return jsonify(status)


@app.route('/annotationcount', methods=['POST'])
@token_required
def api_annotationCount():
    requestParameters = request.get_json()
    status = annotationCount(requestParameters)
    return jsonify(status)


@app.route('/updatemapping', methods=['POST'])
@token_required
def api_updateMapping():
    requestParameters = request.get_json()
    status = updateMapping(requestParameters)
    return jsonify(status)


@app.route('/exportcsv', methods=['POST'])
@token_required
def api_exportCsv():
    requestParameters = request.get_json()
    status = exportCsv(requestParameters)
    return jsonify(status)


@app.route('/subcatconstraints', methods=['POST'])
@token_required
def api_subCategoryConstraints():
    requestParameters = request.get_json()
    status = subCategoryConstraints(requestParameters)
    return jsonify(status)


@app.route('/mfactorconstraints', methods=['POST'])
@token_required
def api_movingFactorConstraints():
    requestParameters = request.get_json()
    status = movingFactorConstraints(requestParameters)
    return jsonify(status)
