import streamlit as st

st.title("Streamlit-App")
st.markdown("Herzlich Willkommen in meiner App. Aktuell ist hier noch nicht viel los.😎")

firstname = st.text_input("Vorname")
lastname = st.text_input("Nachname")

if st.button("Submit"): 
    st.write(firstname + " " + lastname.upper())
