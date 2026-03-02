from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = np.array([[
        data["gender"],
        data["married"],
        data["dependents"],
        data["education"],
        data["selfEmployed"],
        data["creditHistory"],
        data["propertyArea"],
        data["loanTerm"],
        data["loanAmount"],
        data["totalIncome"]
    ]])

    prediction = model.predict(features)[0]

    return jsonify({"result": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)