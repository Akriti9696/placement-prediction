import streamlit as st
import pandas as pd
import pickle
import os
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Placement Prediction System",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# ABOUT PROJECT
# --------------------------------------------------

with st.expander("📘 About This Project"):

    st.markdown("""
    ## 🎓 Placement Prediction System

    This Machine Learning application predicts whether a student
    is likely to be placed based on academic performance,
    technical skills, communication ability, projects, and
    internship experience.

    ### 🔍 Input Features

    - **CGPA** – Academic performance
    - **Programming Score** – Programming/technical ability
    - **Aptitude Score** – Aptitude test performance
    - **Communication Score** – Communication skills
    - **Projects** – Number of completed projects
    - **Internship** – Previous internship experience

    ### 🤖 Prediction

    The trained Machine Learning classification model analyzes
    these features and predicts:

    ✅ **Likely to be PLACED**

    or

    ❌ **Likely to be NOT PLACED**

    The application also displays the model's prediction
    confidence.

    ### 📊 Dashboard

    The application provides:

    - Total predictions
    - Placed students
    - Not placed students
    - Placement distribution
    - Prediction history
    - Searchable prediction records
    """)


# --------------------------------------------------
# CUSTOM THEME
# --------------------------------------------------

st.markdown("""
<style>

    /* Main application background */
    .stApp {
        background: linear-gradient(
            135deg,
            #667eea,
            #764ba2
        );
    }

    /* Main content */
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Main headings */
    h1, h2, h3 {
        color: #333333;
    }

    /* Main title */
    h1 {
        text-align: center;
        font-weight: 700;
    }

    /* White containers/cards */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: white;
        border-radius: 18px;
        padding: 20px;
    }

    /* Buttons */
    .stButton > button {
        background: #4f46e5;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 25px;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: #667eea;
        color: white;
        transform: scale(1.02);
    }

    /* Input boxes */
    div[data-baseweb="input"] {
        border-radius: 10px;
    }

    /* Select box */
    div[data-baseweb="select"] {
        border-radius: 10px;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }

    div[data-testid="stMetricLabel"] {
        color: #666666;
    }

    div[data-testid="stMetricValue"] {
        color: #4f46e5;
    }

    /* Dataframe */
    div[data-testid="stDataFrame"] {
        background: white;
        border-radius: 15px;
        overflow: hidden;
    }

</style>
""", unsafe_allow_html=True)




# --------------------------------------------------
# LOAD MACHINE LEARNING MODEL
# --------------------------------------------------

MODEL_PATH = "models/placement_model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


# --------------------------------------------------
# FILE PATH
# --------------------------------------------------

HISTORY_FILE = "data/prediction_history.csv"


# --------------------------------------------------
# CREATE DATA FOLDER IF NOT EXISTS
# --------------------------------------------------

os.makedirs("data", exist_ok=True)


# --------------------------------------------------
# LOAD HISTORY
# --------------------------------------------------
def get_history():

    columns = [
        "CGPA",
        "Programming",
        "Aptitude",
        "Communication",
        "Projects",
        "Internship",
        "Prediction",
        "Confidence"
    ]

    if not os.path.exists(HISTORY_FILE):
        return pd.DataFrame(columns=columns)

    try:
        history = pd.read_csv(HISTORY_FILE)

        # Make sure all required columns exist
        for column in columns:
            if column not in history.columns:
                history[column] = ""

        # Keep columns in the correct order
        history = history[columns]

        return history

    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        return pd.DataFrame(columns=columns)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎓 Placement Prediction System")

st.write(
    "Machine Learning based application for predicting "
    "student placement outcomes."
)

st.divider()


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.subheader("📋 Enter Student Details")

col1, col2 = st.columns(2)


with col1:

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        step=0.1,
        value=7.0
    )

    programming = st.number_input(
        "Programming Score",
        min_value=0,
        max_value=100,
        value=50
    )

    aptitude = st.number_input(
        "Aptitude Score",
        min_value=0,
        max_value=100,
        value=50
    )


with col2:

    communication = st.number_input(
        "Communication Score",
        min_value=0,
        max_value=100,
        value=50
    )

    projects = st.number_input(
        "Number of Projects",
        min_value=0,
        max_value=10,
        value=1
    )

    internship = st.selectbox(
        "Internship",
        ["Yes", "No"]
    )


st.divider()


# --------------------------------------------------
# PREDICTION BUTTON
# --------------------------------------------------

if st.button(
    "🔮 Predict Placement",
    type="primary",
    use_container_width=True
):

    internship_value = 1 if internship == "Yes" else 0


    # Create DataFrame
    student = pd.DataFrame([{

        "CGPA": cgpa,

        "Programming": programming,

        "Aptitude": aptitude,

        "Communication": communication,

        "Projects": projects,

        "Internship": internship_value

    }])


    # --------------------------------------------------
    # MODEL PREDICTION
    # --------------------------------------------------

    prediction = model.predict(student)

    probability = model.predict_proba(student)

    confidence = round(
        max(probability[0]) * 100,
        2
    )


    # --------------------------------------------------
    # RESULT
    # --------------------------------------------------

    if prediction[0] == 1:

        result = "Student is likely to be PLACED"

        st.success(
            f"🎉 {result}"
        )

    else:

        result = "Student is likely to be NOT PLACED"

        st.error(
            f"❌ {result}"
        )


    # --------------------------------------------------
    # CONFIDENCE
    # --------------------------------------------------

    st.subheader("Prediction Confidence")

    st.progress(
        confidence / 100
    )

    st.write(
        f"**Confidence: {confidence}%**"
    )


    # --------------------------------------------------
    # SAVE PREDICTION
    # --------------------------------------------------

    file_exists = os.path.exists(HISTORY_FILE)

    new_row = pd.DataFrame([{

        "CGPA": cgpa,

        "Programming": programming,

        "Aptitude": aptitude,

        "Communication": communication,

        "Projects": projects,

        "Internship": internship_value,

        "Prediction": result,

        "Confidence": confidence

    }])


    if file_exists:

        history = get_history()

        history = pd.concat(
            [history, new_row],
            ignore_index=True
        )

    else:

        history = new_row


    history.to_csv(
        HISTORY_FILE,
        index=False
    )


    st.success(
        "Prediction saved successfully!"
    )


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

st.divider()

st.subheader("📊 Placement Statistics")


history = get_history()

total_predictions = len(history)


if total_predictions > 0:

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

else:

    placed_students = 0


not_placed = total_predictions - placed_students


# --------------------------------------------------
# STATISTICS CARDS
# --------------------------------------------------

card1, card2, card3 = st.columns(3)


with card1:

    st.metric(
        "Total Predictions",
        total_predictions
    )


with card2:

    st.metric(
        "Placed",
        placed_students
    )


with card3:

    st.metric(
        "Not Placed",
        not_placed
    )


# --------------------------------------------------
# PIE CHART
# --------------------------------------------------

if total_predictions > 0:

    st.subheader("🥧 Placement Distribution")

    chart_data = pd.DataFrame({
        "Status": [
            "Placed",
            "Not Placed"
        ],
        "Students": [
            placed_students,
            not_placed
        ]
    })

    fig = px.pie(
        chart_data,
        names="Status",
        values="Students",
        title="Placed vs Not Placed"
    )

    fig.update_traces(
        textinfo="percent+label",
        hole=0.35,
        marker=dict(
            colors=[
                "#4f46e5",
                "#ef4444"
            ]
        )
    )

    fig.update_layout(
        width=450,
        height=400,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),
        showlegend=True
    )

    st.plotly_chart(
        fig,
        use_container_width=False
    )

    # --------------------------------------------------


# --------------------------------------------------
# PREDICTION HISTORY
# --------------------------------------------------

st.divider()

st.subheader("📋 Prediction History")


if not history.empty:

    display_history = history.copy()

    display_history["Internship"] = (
        display_history["Internship"]
        .map({
            1: "Yes",
            0: "No"
        })
    )

    display_history["Confidence"] = (
        display_history["Confidence"].astype(str) + "%"
    )

    st.dataframe(
        display_history,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No prediction history available yet."
    )

# --------------------------------------------------
# GITHUB PROJECT BUTTON
# --------------------------------------------------

st.markdown("---")

st.markdown(
    "<h3 style='text-align: center;'>Developed by Akriti Pandey</h3>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.link_button(
        "⭐ View Project on GitHub",
        "https://github.com/Akriti9696/placement-prediction",
        use_container_width=True
    )


#--------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Placement Prediction System | "
    "Machine Learning + Python + Streamlit"
)
