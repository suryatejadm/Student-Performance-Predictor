from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    inputs = [float(x) for x in request.form.values()]
    prediction = model.predict([np.array(inputs)])
    result = "Pass" if prediction[0] == 1 else "Fail"
    return render_template("index.html", prediction_text=f"Predicted Result: {result}")

if __name__ == "__main__":
    app.run(debug=True)
