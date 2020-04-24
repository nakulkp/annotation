from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)


def passVerify(pass_key, password):
    try:
        return bcrypt.check_password_hash(pass_key, password)
    except:
        return False;
