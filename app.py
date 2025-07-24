import streamlit as st
import joblib
import numpy as np

model = joblib.load("heart_disease_model.pkl")  # Make sure this file exists in the same directory

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")


st.title("❤️ Heart Disease Prediction App")
st.write("Enter the patient's details below:")

# User Inputs
age = st.slider("Age", 18, 100, 45)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
trestbps = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.slider("Cholesterol (mg/dl)", 100, 600, 250)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["True", "False"])
restecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T Abnormality", "Left Ventricular Hypertrophy"])
thalach = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of the peak exercise ST segment", ["Upsloping", "Flat", "Downsloping"])

#categorical inputs to numerical values
sex = 1 if sex == "Male" else 0
cp_map = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}
cp = cp_map[cp]
fbs = 1 if fbs == "True" else 0
restecg_map = {"Normal": 0, "ST-T Abnormality": 1, "Left Ventricular Hypertrophy": 2}
restecg = restecg_map[restecg]
exang = 1 if exang == "Yes" else 0
slope_map = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
slope = slope_map[slope]


# Predict
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, slope]])

if st.button("Predict"):
    result = model.predict(input_data)
    if result[0] == 1:
        st.error("🚨 High risk of heart disease detected!")
    else:
        st.success("✅ No signs of heart disease detected.")

