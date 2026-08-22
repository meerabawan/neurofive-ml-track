import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("titanic_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="centered"
)

# Title
st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details to predict whether the passenger survived.")

st.divider()

# Passenger information
st.subheader("Passenger Information")

pclass = st.selectbox(
    "Passenger Class",
    [1, 2, 3]
)

name = st.text_input(
    "Passenger Name",
    "John Doe"
)

sex = st.selectbox(
    "Sex",
    ["male", "female"]
)

age = st.number_input(
    "Age",
    min_value=0.0,
    max_value=100.0,
    value=25.0
)

sibsp = st.number_input(
    "Number of Siblings/Spouses Aboard",
    min_value=0,
    max_value=10,
    value=0
)

parch = st.number_input(
    "Number of Parents/Children Aboard",
    min_value=0,
    max_value=10,
    value=0
)

ticket = st.text_input(
    "Ticket Number",
    "A/5 21171"
)

fare = st.number_input(
    "Fare",
    min_value=0.0,
    value=30.0
)

cabin = st.text_input(
    "Cabin",
    ""
)

embarked = st.selectbox(
    "Port of Embarkation",
    ["S", "C", "Q"]
)

st.divider()

# Prediction button
if st.button("Predict Survival"):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "PassengerId": [1],
        "Pclass": [pclass],
        "Name": [name],
        "Sex": [sex],
        "Age": [age],
        "SibSp": [sibsp],
        "Parch": [parch],
        "Ticket": [ticket],
        "Fare": [fare],
        "Cabin": [cabin],
        "Embarked": [embarked]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == 1:
        st.success("🎉 Prediction: Passenger is likely to SURVIVE.")
    else:
        st.error("Prediction: Passenger is likely to NOT SURVIVE.")