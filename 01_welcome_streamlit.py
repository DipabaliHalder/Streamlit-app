import streamlit as st
st.title('Welcome to Streamlit!')
st.write('This is your first Streamlit app. Exciting, right?')

st.title('Streamlit Widgets')

if st.button('Click Me'):
    st.write('Thanks for clicking!')

name = st.text_input('Enter your name:')
if name:
    st.write('Hello, ', name, '!')