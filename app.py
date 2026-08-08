from flask import Flask, render_template, request
import pickle
import csv
import pandas as pd
import os

app = Flask(__name__)


# --------------------------------
# Load Machine Learning Model
# --------------------------------

with open("models/placement_model.pkl", "rb") as file:
    model = pickle.load(file)


# --------------------------------
# Function to get prediction history
# --------------------------------

def get_history():

    file_path = "data/prediction_history.csv"

    # If CSV does not exist
    if not os.path.exists(file_path):

        return pd.DataFrame(
            columns=[
                "CGPA",
                "Programming",
                "Aptitude",
                "Communication",
                "Projects",
                "Internship",
                "Prediction",
                "Confidence"
            ]
        )

    try:

        history = pd.read_csv(file_path)

        return history

    except pd.errors.EmptyDataError:

        return pd.DataFrame(
            columns=[
                "CGPA",
                "Programming",
                "Aptitude",
                "Communication",
                "Projects",
                "Internship",
                "Prediction",
                "Confidence"
            ]
        )


# --------------------------------
# Home Page
# --------------------------------

@app.route("/")
def home():

    history = get_history()

    total_predictions = len(history)

    if total_predictions > 0:

        placed_students = len(
            history[
                history["Prediction"]
                .astype(str)
                .str.contains("PLACED", case=False, na=False)
                &
                ~history["Prediction"]
                .astype(str)
                .str.contains("NOT PLACED", case=False, na=False)
            ]
        )

    else:

        placed_students = 0


    not_placed = total_predictions - placed_students


    history_records = history.to_dict(orient="records")


    return render_template(
        "index.html",
        history=history_records,
        total_predictions=total_predictions,
        placed_students=placed_students,
        not_placed=not_placed
    )


# --------------------------------
# Prediction
# --------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    cgpa = float(request.form["cgpa"])

    programming = int(request.form["programming"])

    aptitude = int(request.form["aptitude"])

    communication = int(request.form["communication"])

    projects = int(request.form["projects"])

    internship = int(request.form["internship"])


    # Create DataFrame
    student = pd.DataFrame([{

        "CGPA": cgpa,

        "Programming": programming,

        "Aptitude": aptitude,

        "Communication": communication,

        "Projects": projects,

        "Internship": internship

    }])


    # Make prediction
    prediction = model.predict(student)


    # Prediction probability
    probability = model.predict_proba(student)


    confidence = round(
        max(probability[0]) * 100,
        2
    )


    # Result
    if prediction[0] == 1:

        result = "Student is likely to be PLACED"

    else:

        result = "Student is likely to be NOT PLACED"


    # --------------------------------
    # Save prediction to CSV
    # --------------------------------

    file_path = "data/prediction_history.csv"


    file_exists = os.path.exists(file_path)


    with open(
        file_path,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)


        # Add header if file is new
        if not file_exists:

            writer.writerow([
                "CGPA",
                "Programming",
                "Aptitude",
                "Communication",
                "Projects",
                "Internship",
                "Prediction",
                "Confidence"
            ])


        writer.writerow([

            cgpa,

            programming,

            aptitude,

            communication,

            projects,

            internship,

            result,

            confidence

        ])


    # --------------------------------
    # Read updated history
    # --------------------------------

    history = get_history()


    total_predictions = len(history)


    # Count placed students
    placed_students = len(
        history[
            history["Prediction"]
            .astype(str)
            .str.contains(
                "PLACED",
                case=False,
                na=False
            )
            &
            ~history["Prediction"]
            .astype(str)
            .str.contains(
                "NOT PLACED",
                case=False,
                na=False
            )
        ]
    )


    # Count not placed
    not_placed = total_predictions - placed_students


    # Convert history to dictionary
    history_records = history.to_dict(
        orient="records"
    )


    # --------------------------------
    # Send data to HTML
    # --------------------------------

    return render_template(

        "index.html",

        prediction=result,

        confidence=confidence,

        history=history_records,

        total_predictions=total_predictions,

        placed_students=placed_students,

        not_placed=not_placed

    )


# --------------------------------
# Run Flask
# --------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)