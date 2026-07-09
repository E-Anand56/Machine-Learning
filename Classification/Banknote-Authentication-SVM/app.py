import streamlit as st
import joblib
import numpy as np

# Load pipeline
model = joblib.load("svm_pipeline.pkl")

st.title("Banknote Authentication")

variance = st.number_input("Variance")
skewness = st.number_input("Skewness")
kurtosis = st.number_input("Kurtosis")
entropy = st.number_input("Entropy")

if st.button("Predict"):

    sample = np.array([[variance, skewness, kurtosis, entropy]])

    prediction = model.predict(sample)

    if prediction[0] == 0:
        st.success("✅ Genuine Banknote")
    else:
        st.error("❌ Fake Banknote")