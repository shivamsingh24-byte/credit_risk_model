import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/credit_risk_model.pkl")

st.set_page_config(page_title="Credit Risk Prediction", layout="centered")

st.title("Credit Risk Prediction System")
st.write("Enter the applicant details below to predict the loan default risk.")

# User Inputs
person_age = st.number_input("Age", min_value=18, max_value=100, value=25)

person_income = st.number_input("Annual Income", min_value=0.0, value=50000.0)

person_home_ownership = st.selectbox(
    "Home Ownership",
    ["MORTGAGE", "OWN", "RENT", "OTHER"]
)

person_emp_length = st.number_input(
    "Employment Length (Years)",
    min_value=0.0,
    value=5.0
)

loan_intent = st.selectbox(
    "Loan Purpose",
    [
        "DEBTCONSOLIDATION",
        "EDUCATION",
        "HOMEIMPROVEMENT",
        "MEDICAL",
        "PERSONAL",
        "VENTURE"
    ]
)

loan_grade = st.selectbox(
    "Loan Grade",
    ["A", "B", "C", "D", "E", "F", "G"]
)

loan_amnt = st.number_input("Loan Amount", min_value=0.0, value=10000.0)

loan_int_rate = st.number_input(
    "Interest Rate (%)",
    min_value=0.0,
    value=10.5
)

loan_percent_income = st.number_input(
    "Loan Percent Income",
    min_value=0.0,
    value=0.20
)

cb_person_default_on_file = st.selectbox(
    "Previous Default",
    ["N", "Y"]
)

cb_person_cred_hist_length = st.number_input(
    "Credit History Length",
    min_value=0,
    value=5
)

# Encoding dictionaries
home_map = {
    "MORTGAGE": 0,
    "OTHER": 1,
    "OWN": 2,
    "RENT": 3
}

intent_map = {
    "DEBTCONSOLIDATION": 0,
    "EDUCATION": 1,
    "HOMEIMPROVEMENT": 2,
    "MEDICAL": 3,
    "PERSONAL": 4,
    "VENTURE": 5
}

grade_map = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6
}

default_map = {
    "N": 0,
    "Y": 1
}

if st.button("Predict Risk"):

    input_data = pd.DataFrame({
        "person_age":[person_age],
        "person_income":[person_income],
        "person_home_ownership":[home_map[person_home_ownership]],
        "person_emp_length":[person_emp_length],
        "loan_intent":[intent_map[loan_intent]],
        "loan_grade":[grade_map[loan_grade]],
        "loan_amnt":[loan_amnt],
        "loan_int_rate":[loan_int_rate],
        "loan_percent_income":[loan_percent_income],
        "cb_person_default_on_file":[default_map[cb_person_default_on_file]],
        "cb_person_cred_hist_length":[cb_person_cred_hist_length]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("High Credit Risk (Likely to Default)")
    else:
        st.success("Low Credit Risk (Not Likely to Default)")

    st.write(f"Default Probability: **{probability:.2%}**")
    