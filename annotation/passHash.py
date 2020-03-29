from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)


def passHash(password):
    return bcrypt.generate_password_hash(password).decode("utf-8")
