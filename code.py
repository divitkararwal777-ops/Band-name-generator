import streamlit as st

st.title("🎸 Band Name Generator")

st.write("Welcome to the Band Name Generator!")

city = st.text_input("What's the name of the city you grew up in?")
pet = st.text_input("What's the name of your pet?")

if st.button("Generate Band Name"):
    if city and pet:
        st.success(f"Your band name could be {city} {pet} 🎵")
    else:
        st.warning("Please enter both your city and pet name.")
