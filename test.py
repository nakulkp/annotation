import os
import hashlib

# Example generation
salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', 'mypassword'.encode('utf-8'), salt, 100000)

# Store them as:
storage = salt + key
print(salt.decode("UTF-8"))
salt = str(salt)
print(type(salt))
print(salt)
print("conv")
salt = salt[2:-1]
salt = salt
print(salt)
print("byte")
salt = salt.encode('UTF-8')
print(salt)

# Getting the values back out
salt_from_storage = storage[:32]  # 32 is the length of the salt
key_from_storage = storage[32:]
