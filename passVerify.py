import hashlib


# returns true if password hash match

def passVerify(pass_key, password):
    new_key = hash(password)

    if new_key == pass_key:
        return True
    else:
        return False
