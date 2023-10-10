from flask import Flask, render_template, request
import RGBimage
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')
@app.route('/upload', methods=['POST'])
def getValue():
    image = request.form['input-file']
    print(image)
    rgb = RGBimage.getRGB(image)
    print(rgb)
    return "File uploaded successfully!"
@app.route('/response')
def response():
    return render_template('response.html')
if __name__ == '__main__':
    app.run(debug=True)