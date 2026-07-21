from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # यह ब्राउज़र और सर्वर की सभी रुकावटों को खत्म कर देगा

database = {"data": "अभी कोई डेटा नहीं है"}
APP_PASSWORD = "1234"      
DATA_PASSWORD = "5678"     

@app.route('/login', methods=['POST'])
def login():
    req = request.json
    if req.get('password') == APP_PASSWORD:
        return jsonify({"status": "success", "message": "Login successful"})
    return jsonify({"status": "error", "message": "गलत पासवर्ड!"}), 401

@app.route('/get-data', methods=['POST'])
def get_data():
    req = request.json
    if req.get('data_password') != DATA_PASSWORD:
        return jsonify({"error": "डेटा देखने के लिए गलत पासवर्ड है!"}), 401
    return jsonify(database)

@app.route('/post-data', methods=['POST'])
def post_data():
    req = request.json
    if req.get('data_password') != DATA_PASSWORD:
        return jsonify({"error": "डेटा भेजने के लिए गलत पासवर्ड है!"}), 401
        
    req_data = req.get('data', '')
    if len(req_data.encode('utf-8')) > 1024 * 1024:
        return jsonify({"error": "डेटा 1 MB से बड़ा है!"}), 400
        
    database["data"] = req_data
    return jsonify({"status": "सफलतापूर्वक डेटा सेव हो गया!", "data": database["data"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=
