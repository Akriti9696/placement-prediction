from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("models/placement_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    cgpa = float(request.form["cgpa"])
    programming = int(request.form["programming"])
    aptitude = int(request.form["aptitude"])
    communication = int(request.form["communication"])
    projects = int(request.form["projects"])
    internship = int(request.form["internship"])

    student = [[
        cgpa,
        programming,
        aptitude,
        communication,
        projects,
        internship
    ]]

    prediction = model.predict(student)

    probability = model.predict_proba(student)

    confidence = round(max(probability[0]) * 100, 2)

    if prediction[0] == 1:
        result = "🎉 Student is likely to be PLACED"
    else:
        result = "❌ Student is likely to be NOT PLACED"

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)