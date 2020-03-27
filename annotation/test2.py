from flask import Flask, request, jsonify

from annotation.csvUpload import csvUpload

app = Flask(__name__)
app.config["DEBUG"] = True

lst = [1,2,3,4,5]
popVal = lst.pop()

print(lst)
print(popVal)

@app.route('/csvupload', methods=['POST'])
def api_csvUpload():
    requestParameters = request.get_json()

    status = csvUpload(requestParameters)
    return jsonify(status)

#app.run()