import hashlib


# returns true if password hash match

def passVerify(salt, key, password):
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    if new_key == key:
        return True
    else:
        return False
