def passVerify(pass_key, password):
    new_key = password

    if new_key == pass_key:
        return True
    else:
        return False
