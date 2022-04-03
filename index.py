from email.mime import image
from flask import Flask, render_template, request
# from math_ocr import predict

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    request_data = request.data
    image = request_data.decode()
    # prediction = predict(image)
    print(image)
    return "Predicting"