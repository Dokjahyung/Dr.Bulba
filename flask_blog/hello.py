from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import RGBimage
import os
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')
@app.route('/upload', methods=['POST'])
def getValue():
    uploaded_file = request.files['input-file']
    # Check if a file was actually uploaded
    if uploaded_file.filename != '':
        # Save the uploaded file to a temporary location or process it
        # For example, you can save it using secure_filename and store it in a folder
        upload_folder = os.path.join(os.getcwd(), 'static', 'img')
        # Make sure the directory exists, if not, create it
        os.makedirs(upload_folder, exist_ok=True)
        # Save the uploaded file
        uploaded_file.save(os.path.join(upload_folder, secure_filename(uploaded_file.filename)))


        # Now you can pass the file path to your getRGB function
        image_path = os.path.join('static', 'img', secure_filename(uploaded_file.filename))

        rgb = RGBimage.getRGB(image_path)
        print(rgb)

        return "File uploaded successfully!"
    else:
        return "No file uploaded"
@app.route('/response')
def response():
    return render_template('response.html')
if __name__ == '__main__':
    app.run(debug=True)
