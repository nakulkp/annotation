from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)


def passHash(password):
    pass_key = bcrypt.generate_password_hash(password).decode("utf-8")
    return pass_key


def passVerify(pass_key, password):
    return bcrypt.check_password_hash(pass_key, password)



password = "test"

pass_key = passHash(password)
print(pass_key)

print(passVerify(pass_key, password))
