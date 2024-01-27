from flask import Flask, request
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']

    # If the user submits an empty file, handle it accordingly
    if file.filename == '':
        return 'No selected file', 400

    # Use secure_filename to sanitize the filename
    filename = secure_filename(file.filename)

    # Save the file to the uploads folder (create the folder if not exists)
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)

    file.save(os.path.join(upload_folder, file.filename))

    return 'File successfully uploaded', 200

if __name__ == '__main__':
    app.run(debug=True, port=6666, host='0.0.0.0')


