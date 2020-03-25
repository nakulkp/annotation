from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

uName = 'valkyrie'
passWord = 'pass'
@app.route('/jwtlogin')
def api_jwtLogin():
    auth =request.authorization
    if auth and auth.username == uName  and auth.password == passWord:
        return "success"
    else:
        return "nah"


if __name__==('__main__'):
    app.run(debug=True)
