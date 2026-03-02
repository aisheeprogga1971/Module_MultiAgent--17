
from agent import agent
import streamlit as st

st.title("Place Finder AI")

user_query = st.text_input("Ask about restaurants,hospitals or institutions:")

if user_query:
    response = agent.run(user_query)
    st.write(response)

