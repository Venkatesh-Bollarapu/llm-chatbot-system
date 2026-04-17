import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage

load_dotenv()

st.title("Chat App")

model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")

user_ip = st.chat_input("Ask anything")

if user_ip:
    with st.chat_message("user"):
        st.write(user_ip)

    response = model.invoke([HumanMessage(content=user_ip)])

    with st.chat_message("assistant"):
        st.write(response.content)

