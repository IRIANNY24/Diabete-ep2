import streamlit as st
import joblib
import numpy as np

modelo = joblib.load("modelo_logistico.pkl")

st.title("Predicción de Diabetes")

st.write("Nombre: Irianny Ardila")
st.write("Código ISIL:6816")

st.write("https://colab.research.google.com/drive/1eXs8_VSXKG60FxBS25mzNVGiunzDciAv?usp=sharing")

pregnancies = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
bloodpressure = st.number_input("BloodPressure")
skinthickness = st.number_input("SkinThickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("DiabetesPedigreeFunction")
age = st.number_input("Age")

if st.button("Predecir"):

    datos = np.array([[pregnancies, glucose, bloodpressure,
                       skinthickness, insulin, bmi, dpf, age]])

    prediccion = modelo.predict(datos)

    if prediccion[0] == 1:
        st.error("La persona tiene diabetes")
    else:
        st.success("La persona no tiene diabetes")
