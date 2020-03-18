import flask
from flask import request, jsonify
import psycopg2
from config import config
from login import login
from userSignUp import userSignUp

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
    print(requestParameters)
    signUpStatus = userSignUp(requestParameters)
    print(signUpStatus)
    return jsonify(requestParameters)


@app.route('/login', methods=['GET'])
def api_login():
    requestParameters = request.args
    username = requestParameters.get('username')
    password = requestParameters.get('password')
    loginStatus = login(username, password)

    return jsonify(loginStatus)


@app.route('/articlecontent', methods=['GET'])
def api_articleById():
    requestParameters = request.args  # takes args from request

    id = requestParameters.get('id')
    flag = requestParameters.get('flag')

    query = "SELECT content FROM master_table WHERE"
    # cursor.execute("SELECT admin FROM users WHERE username = %(username)s", {'username': username});
    if id:
        query += ' user_id= %(username)s AND status=todo'

    if not (id):
        return page_not_found(404)

    # query = query[:-4] + ';'  # clip off the trailing AND query

    # Connecting to PostgreSQL server
    params = config()
    conn = psycopg2.connect(**params)  # connect to DB

    cur = conn.cursor()
    cur.execute(query, {'username': id})
    result = cur.fetchall()

    # Commiting, and Closing DB Connection
    cur.close()
    conn.commit()  # Commit Changes
    conn.close()

    return jsonify(result)


app.run()
