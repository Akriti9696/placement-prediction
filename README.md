# 🎓 Placement Prediction System

A Machine Learning based web application that predicts whether a student is likely to be placed based on academic performance, programming skills, aptitude, communication skills, projects, and internship experience.

The project combines **Python, Machine Learning, Flask, HTML, CSS and JavaScript** to provide an interactive placement prediction dashboard.

---

## 📌 Project Overview

The Placement Prediction System takes student information as input and uses a trained Machine Learning model to predict the student's placement outcome.

The application also provides:

- Placement prediction
- Prediction confidence
- Total prediction statistics
- Placed vs Not Placed statistics
- Interactive placement chart
- Prediction history
- Searchable prediction table
- Responsive web interface

---

## 🚀 Features

### 🤖 Machine Learning Prediction

The application predicts whether a student is likely to be:

- ✅ PLACED
- ❌ NOT PLACED

### 📊 Confidence Score

The application displays the model's prediction confidence as a percentage.

### 📈 Placement Statistics

The dashboard displays:

- Total Predictions
- Placed Students
- Not Placed Students

### 🥧 Placement Chart

An interactive chart shows the distribution between:

- Placed students
- Not placed students

### 📋 Prediction History

Every prediction can be stored and displayed in a table containing:

- CGPA
- Programming Score
- Aptitude Score
- Communication Score
- Number of Projects
- Internship
- Prediction
- Confidence

### 🔎 Search

The prediction history table includes a search feature for quickly finding records.

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Pandas
- NumPy

### Web Development

- Flask
- HTML5
- CSS3
- JavaScript

### Data Storage

- CSV

### Development Tools

- VS Code
- Jupyter Notebook
- Git
- GitHub

---

## 🧠 Machine Learning Model

The project uses a **Logistic Regression** model for binary classification.

### Input Features

The model uses:

| Feature | Description |
|---|---|
| CGPA | Student's CGPA |
| Programming | Programming skill score |
| Aptitude | Aptitude test score |
| Communication | Communication score |
| Projects | Number of projects |
| Internship | Internship experience |

### Output

The model predicts one of two outcomes:

```text
PLACED
NOT PLACED