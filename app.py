import streamlit as st

st.title("🍻 Alcohol Predictor")
st.write("This app predicts total alcohol consumption based on beverage servings.")

beer = st.number_input("Beer Servings", min_value=0, max_value=500, value=100)
spirit = st.number_input("Spirit Servings", min_value=0, max_value=500, value=50)
wine = st.number_input("Wine Servings", min_value=0, max_value=500, value=80)
continent = st.selectbox("Continent", ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America'])

if st.button("Predict"):
    st.success("Prediction logic will go here!")