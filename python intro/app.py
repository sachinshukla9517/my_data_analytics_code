import streamlit as st
st.title("my  streamlit app")
st.header("this is a Header")
st.subheader("a subheader")
st.text("small text")
st.text_input("Enter your name")
st.checkbox("Do you agree>?")
st.button("click to fly!!")

sidebar = st.sidebar
sidebar.title("Sidebar Title")
age = sidebar.text_input("Enter your age:")
btn2 = sidebar.button("Sachin shukla")
if btn2:
    st.balloons()
    