from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_feedback():
    data = request.json
    print("Received Feedback:", data)
    return jsonify({"status": "received"}), 200
