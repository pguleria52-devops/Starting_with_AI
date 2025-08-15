import streamlit as st

st.title('Streamlit Text Input')

name = st.text_input("Enter your name:")

age = st.slider("Select Your age: ",0,100,25)

st.write(f"Your age is {age}.")

options = ['Python','Java','C++','JavaScript']
choice = st.selectbox("Choose your favorite language:",options)
st.write(f"Your selected language {choice}")

if name:
    st.write(f"Hello, {name}")