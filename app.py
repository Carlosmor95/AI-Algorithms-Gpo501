from flask import Flask, jsonify, request
from FFN import train_and_save_model
import dijkstra

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message='Hello, World!')

@app.route('/ffn', methods=['GET','POST'])
def test():
    if request.method == "GET":
        return jsonify({"response": "Get Request Called"})
    elif request.method == "POST":
        req_Json = request.json
        return train_and_save_model(req_Json, 'saved_model')

@app.route('/dijkstra', methods=['POST'])
def run_dijkstra():
    req_Json = request.json
    graph = req_Json['graph']
    startNode = req_Json['startNode']
    endNode = req_Json['endNode']
    result = dijkstra.solve(graph, startNode, endNode)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
