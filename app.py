from flask import Flask, jsonify, request
from FFN import train_and_save_model

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message='Hello, World!')

@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == "GET":
        return jsonify({"response": "Get Request Called"})
    elif request.method == "POST":
        req_Json = request.json
        #name = req_Json['name']
        train_and_save_model(req_Json, 'saved_model')
        return jsonify({"response": "Hi"})

if __name__ == '__main__':
    app.run(debug=True)
