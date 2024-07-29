from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/flights', methods=['GET'])
def get_flights():
    with open('mock_data.json') as f:
        flights = json.load(f)
    return jsonify(flights)

if __name__ == '__main__':
    app.run(debug=True)
