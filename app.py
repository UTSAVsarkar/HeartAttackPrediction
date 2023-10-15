import streamlit as st
from about_page import about
from predict_page import predict_page
from explore_page import explore_page

st.title("Heart Diseases Predictor 🩺❤️")
st.write("""### Predict and Explore the data 🤟""")

aboutPage, predictPage, explorePage = st.tabs(["About", "Predict", "Explore"])

with aboutPage:
   about()

with predictPage:
   predict_page()

with explorePage:
   explore_page()