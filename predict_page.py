import pickle
import numpy as np
import streamlit as st

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
scaler= data["scaler"]


def checker(age, trestbps, chol, thalachh, oldPeak):
    return age=='' or trestbps=='' or chol=='' or thalachh=='' or oldPeak==''

def predict_page():
    age = st.text_input('**Age**', placeholder="Age")

    sex = st.radio(
        "**Sex**",
        [1, 0],
        captions=  ["Male", "Female"],
        horizontal = True
    )

    cp = st.radio(
        "**Chest pain type**",
        [1, 2, 3, 4],
        captions = ["Aypical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"],
        horizontal = True
    )

    trestbps = st.text_input('**Resting blood pressure**', placeholder = "(in mm Hg)")

    chol = st.text_input('**Cholesterol level**', placeholder = "eg. 250")

    fbs = st.radio(
        "**Fasting blood sugar > 120 mg/dl**",
        [1, 0],
        captions = ["True", "False"],
        horizontal = True
    )

    restecg = st.radio(
        "**Resting electrocardiographic results**",
        [0, 1, 2],
        captions = ["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"],
        horizontal = True
    )

    thalachh = st.text_input('**Maximum heart rate achieved**', placeholder = "eg. 150")

    exang = st.radio(
        "**Exercise-induced angina**",
        [1, 0],
        captions = ["Yes", "No"],
        horizontal = True
    )

    oldPeak = st.text_input("Previous Peak", placeholder = "eg. 2.6")

    slp = st.radio(
        "**Slope**",
        [0, 1, 2, ],
        horizontal = True
    )

    caa = st.radio(
        "**Number of major vessels**",
        [0 ,1 ,2 ,3, 4],
        horizontal = True
    )

    thall = st.radio(
        "**Thalium Stress Test result**",
        [0, 1, 2, 3],
        horizontal = True
    )

    ok = st.button("Predict")

    if ok:
        if(checker(age, trestbps, chol, thalachh, oldPeak)):
            st.error('Please enter all the parameters!', icon="🚨")
        else:
            X = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalachh, exang, oldPeak, slp, caa, thall]])
            X = scaler.transform(X)

            output = model.predict(X)

            if(output[0] == 0):
                st.subheader("You have less chance of heart attack 😇")
            else:
                st.subheader("You have more chance of heart attack 😧")

            st.write("""### 👈 To know more about the dataset, go to About page""")
