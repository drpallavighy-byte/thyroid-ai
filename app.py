import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("thyroid_model.pkl")

st.title("Thyroid Disease Prediction")

# User inputs
ft3 = st.number_input("Enter FT3 value (pg/mL):")
ft4 = st.number_input("Enter FT4 value (ng/dL):")
tsh = st.number_input("Enter TSH value (µIU/mL):")

if st.button("Predict"):
    input_data = pd.DataFrame([[ft3, ft4, tsh]], columns=["FT3", "FT4", "TSH"])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Diagnosis: {prediction}")
