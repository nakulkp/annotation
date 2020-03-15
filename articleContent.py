"""

fn call -- userId flag
	flag init 0
	query article where userID - todo
		flag ==0=> fetch first
		flag !=1=> take todo flag value
		import	data from table

"""

import flask
from flask import request, jsonify
import psycopg2
from config import config

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '<h1> HOME </h1>'


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Requested Resource Not Found!!!</p>", 404


@app.route('/articlecontent', methods=['GET'])
def api_articleById():
    requestParameters = request.args  # takes args from request

    id = requestParameters.get('id')
    flag = requestParameters.get('flag')

    query = "SELECT " + article_id + " FROM master_table WHERE"

    if id:
        query += ' user_id=' + id + ' AND status=todo'

    if not (id):
        return page_not_found(404)

    # query = query[:-4] + ';'  # clip off the trailing AND query

    # Connecting to PostgreSQL server
    params = config()
    conn = psycopg2.connect(**params)  # connect to DB

    cur = conn.cursor()
    cur.execute(query)

    articleId = cur.fetchall()  # returns list of articles
    article = articleId[flag]
    query = "SELECT content FROM master_table WHERE article_id=" + article
    cur.execute(query)

    result = cur.fetchall()

    # Commiting, and Closing DB Connection
    cur.close()
    conn.commit()  # Commit Changes
    conn.close()

    return jsonify(result)


app.run()
