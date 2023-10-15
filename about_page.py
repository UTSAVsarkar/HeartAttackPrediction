import streamlit as st

def about():
        st.write("""###
**Description:** This dataset contains various health-related features and their corresponding values for a group of patients. The dataset is designed for predicting the likelihood of a heart attack in a patient.

**Features:**
1. **Age:** Age of the patient.
2. **Sex:** Gender of the patient (1 = male, 0 = female).
3. **Exang:** Exercise-induced angina (1 = yes, 0 = no).
4. **CA:** Number of major vessels (ranging from 0 to 3).
5. **CP:** Chest pain type (1 = typical angina, 2 = atypical angina, 3 = non-anginal pain, 4 = asymptomatic).
6. **Trestbps:** Resting blood pressure (in mm Hg).
7. **Chol:** Cholesterol level in mg/dL.
8. **FBS:** Fasting blood sugar level (1 = >120 mg/dL, 0 = <=120 mg/dL).
9. **Rest ECG:** Resting electrocardiographic results (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria).
10. **Thalach:** Maximum heart rate achieved.
11. **Target:** The target variable that indicates the likelihood of a heart attack (0 = less chance of a heart attack, 1 = more chance of a heart attack).

**Purpose:** The dataset is commonly used for training machine learning models to predict the risk of heart disease in patients based on their health attributes. Researchers and healthcare professionals may use this dataset to develop predictive models for early heart disease detection.             
               """)
        
        st.subheader('', divider='rainbow')
        
        st.write("""### 
                 
**Certainly, here's some information about the dataset:**

**Dataset Source:** This dataset may have been sourced from medical records, clinical studies, or surveys conducted in the field of cardiology and healthcare.

**Size:** The size of the dataset can vary, but it typically contains a moderate number of rows and columns, making it suitable for machine learning and statistical analysis.

**Unique Characteristics:**
- The dataset includes a mix of numerical and categorical features, allowing for a diverse range of analyses.
- It contains information about patients' health metrics, exercise-induced symptoms, and diagnostic test results.
- The target variable, "target," serves as the main focus for classification tasks, with values 0 and 1 representing different levels of heart attack risk.
- The dataset can be used for tasks such as classification, regression, and data exploration in the context of heart disease prediction and risk assessment.

**Insights:**
- Data scientists and healthcare professionals can use this dataset to build predictive models for heart disease risk assessment. Machine learning algorithms can be trained to identify patterns and factors that contribute to heart disease, enabling early intervention.
- The dataset provides a valuable resource for research in cardiology, allowing for the exploration of the relationships between various health factors and the likelihood of heart attacks.
- Visualization and statistical analysis of the dataset may reveal trends and correlations between features and the target variable.

**Data Usage:** Researchers and data scientists can employ this dataset to:
- Develop predictive models to estimate the likelihood of a patient experiencing a heart attack based on their health profile.
- Investigate the impact of different features, such as age, gender, blood pressure, and cholesterol, on heart disease risk.
- Create data-driven insights to support clinical decision-making and public health initiatives.
                 """)
        
        st.subheader('', divider='rainbow')
