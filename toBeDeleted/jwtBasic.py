import jwt
#jwt.encode(msg,secretKey,algorithmName) if algo name not specified, then default alog is used

secretKey = "g3z4N_6(0wdB"
signedToken = jwt.encode({'data to':'be verfied'},secretKey)
print(str(signedToken))

verify = jwt.decode(signedToken,secretKey)
print(verify)