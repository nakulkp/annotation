import hashlib
import os


# salt = random generated
# key = hashed password
# save both

def passHash(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt, key
