from pyexpat import model
import pickle
from flask import Flask, render_template, request, redirect

from predict import emotion_prediction

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/predict", methods = ['POST','GET'])
def predict_func():
    if request.method == "POST":
        file = request.files["filename"]
        emotion, accuracy = emotion_prediction(file)
        return render_template('predict.html', emotion=emotion, accuracy=accuracy)

    return render_template('predict.html')



if __name__ == "__main__":
    app.run(debug=True)