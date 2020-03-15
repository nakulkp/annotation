from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({'text': 'Hello World!'})

@app.route("/login")
def login():
    print("Login Page")
    return jsonify({'text':'Login page'})

if __name__ == '__main__':
    print("running")
    app.run(port=5022)
