from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return 'Uploaded', 200

@app.route('/files', methods=['GET'])
def list_files():
    return jsonify(os.listdir(UPLOAD_FOLDER))

@app.route('/uploads/<filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run()
