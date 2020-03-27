from flask import Flask, request, jsonify
import jwt
import datetime

from functools import wraps

from annotation.login import login

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "!5@adjh@#!@QSQsw1!@c"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.get_json('token')
        if not token:
            return jsonify({'message': 'token missing'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Invalid Token'}), 403
        return f(*args, **kwargs)

    return decorated

@app.route('/home', methods=['POST'])
@token_required
def home():
    return "HOME"


@app.route('/login', methods=['POST'])
def api_login():
    requestParameters = request.get_json()
    # loginStatus = login(requestParameters)
    authenticated = {"auth": "success"}
    email = requestParameters['email']
    # authenticated = loginStatus.pop()
    if authenticated['auth'] == 'success':
        token = jwt.encode(
            {'email': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config["SECRET_KEY"])
        return jsonify({'token': token.decode('UTF-8')})
    # return jsonify(loginStatus)


app.run()
