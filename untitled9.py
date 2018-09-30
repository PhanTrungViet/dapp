from flask import Flask, jsonify, request
from database import *
import json
import datetime

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def hello_world():
    return jsonify(request.json)

@app.route('/questions')
def questions():
    results = getQuestions()
    return json.dumps(results)

@app.route('/users')
def users():
    users = getUsers()
    return json.dumps(users)

@app.route('/user/add', methods=['POST', 'GET'])
def adduser():
    if request.method == 'POST':
        data = request.get_json()
        idcard = data["idcard"]
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        address = data["address"]
        privateKey = data["privateKey"]
        results = addUser(idcard, name, email, phone, address, privateKey)
        return json.dumps(results)


@app.route('/results', methods=['POST', 'GET'])
def results():
    results = getResults()
    return json.dumps(results)

@app.route('/result/add', methods=['POST', 'GET'])
def addresult():
    if request.method == 'POST':
        data = request.get_json()
        point = data["point"]
        idcard = data["idcard"]
        content = data["content"]
        id = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        result = addResult(id, point, idcard, content)
        return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True, port=3000)