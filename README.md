# 🎓 Placement Prediction System

A Machine Learning web application that predicts whether a student is likely to be placed based on their academic and skill-related information.


## 🚀 Live Demo

👉 [Open Placement Prediction App](https://placement-prediction-by-akritipandey.streamlit.app/)

## 📌 Features

- Student placement prediction
- CGPA-based prediction
- Programming score analysis
- Aptitude score analysis
- Communication score analysis
- Project count
- Internship status
- Prediction confidence percentage
- Placement statistics
- Interactive pie chart
- Prediction history
- Searchable prediction history
- Responsive and user-friendly interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly
- Pickle
- Git & GitHub

## 🤖 Machine Learning

The application uses a trained Machine Learning classification model to predict the placement status of students.

### Input Features

- CGPA
- Programming Score
- Aptitude Score
- Communication Score
- Number of Projects
- Internship Status

### Output

The model predicts:

- ✅ Student is likely to be PLACED
- ❌ Student is likely to be NOT PLACED

The application also displays the model's prediction confidence.

## 📊 Dashboard

The application provides:

- Total Predictions
- Placed Students
- Not Placed Students
- Placement Distribution
- Prediction History

## 📂 Project Structure

```text
Placement Prediction/
│
├── models/
│   └── placement_model.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── streamlit_app.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore