import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/fraud_detection_model.pkl")

# Page settings
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Card Fraud Detection")
st.write(
    "Enter the transaction details below to predict whether "
    "the transaction is legitimate or potentially fraudulent."
)

st.divider()

# Get exact feature names from the trained model
features = model.feature_names_in_

# Create input fields
input_data = {}

for feature in features:
    input_data[feature] = st.number_input(
        feature,
        value=0.0,
        format="%.6f"
    )

# Prediction button
if st.button("🔍 Detect Fraud", use_container_width=True):

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    st.divider()

    if prediction == 1:
        st.error("⚠️ Potential Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction Appears Legitimate")