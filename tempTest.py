from passHash import passHash
from passVerify import passVerify

salt, key = passHash("nakul")

if string == salt:
    print("succ")
else:
    print("not succ")
