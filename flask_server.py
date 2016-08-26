from flask import Flask, request, json, jsonify
import benchmark

app = Flask(__name__)

@app.route('/')
def root():
    return('FLASK SERVER')

@app.route('/api/algos', methods=['POST'])
def run():
    data = request.get_json(force=True)
    lengthArr = data['lengthArr']
    request_data = data['request_data']
    name = data['request_data']['name']
    result = benchmark.handle_request(lengthArr, request_data)
    response_data = {"xAxis": lengthArr, "name": name, "rawData": result}
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(port=int('8002'))
