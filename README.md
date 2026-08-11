# 🎓 Placement Prediction System

A Machine Learning based web application that predicts whether a student is likely to be placed based on academic performance, technical skills, communication skills, projects, and internship experience.

The application is built using **Python, Machine Learning, Pandas, Scikit-learn, Plotly, and Streamlit**.

## 🚀 Live Demo

👉 https://placement-prediction-by-akritipandey.streamlit.app/

## 📂 GitHub Repository

👉 https://github.com/Akriti9696/placement-prediction

---

## 📌 Project Overview

The Placement Prediction System uses a trained **Logistic Regression** classification model to predict student placement outcomes.

The user provides:

- CGPA
- Programming Score
- Aptitude Score
- Communication Score
- Number of Projects
- Internship Experience

The trained model then predicts whether the student is likely to be:

✅ **Placed**

or

❌ **Not Placed**

The application also calculates the model's prediction confidence.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Logistic Regression
- Plotly
- Streamlit
- Pickle
- Git & GitHub

---

## 📊 Application Features

### 🎓 Student Prediction

Users can enter student information and receive an immediate placement prediction.

### 📈 Prediction Confidence

The application displays the confidence percentage associated with the prediction.

### 📊 Placement Dashboard

The dashboard displays:

- Total Predictions
- Placed Students
- Not Placed Students
- Placement Distribution

### 🥧 Interactive Pie Chart

A Plotly-based pie chart visualizes the distribution of placed and not-placed predictions.

### 📋 Prediction History

The application stores previous predictions and displays them in a searchable table.

### 🎨 Custom UI

The application includes a custom gradient theme, styled cards, buttons, metrics, and responsive layout.

---

## 🧠 Machine Learning Workflow

The project follows these steps:

```text
Dataset
   ↓
Data Exploration
   ↓
Data Visualization
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Logistic Regression
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
Streamlit Deployment