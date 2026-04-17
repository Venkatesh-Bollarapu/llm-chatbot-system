from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langgraph.graph.message import BaseMessage,add_messages
from langchain.messages import HumanMessage,AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()

class State(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

# model = ChatGoogleGenerativeAI(model = "models/gemini-2.5-flash")
llm = HuggingFaceEndpoint(
  repo_id="meta-llama/Llama-3.1-8B-Instruct",
  task = "text-generation"
)
model = ChatHuggingFace(llm = llm)
def chat_gen(state:State):
    response = model.invoke(state['messages'])
    return {"messages":[response]}



checkpointer = MemorySaver()
graph = StateGraph(State)
#nodes
graph.add_node("chat_gen",chat_gen)
#edges
graph.add_edge(START,"chat_gen")
graph.add_edge("chat_gen",END)

chatbot = graph.compile(checkpointer = checkpointer)

st.title('chat App')

user_ip = st.chat_input('ask anything')

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for chat in st.session_state["messages"]:
    with st.chat_message(chat["role"]):
        st.write(chat['msg'])


lc_message = []


thread_id = '1'
if user_ip:
    with st.chat_message("user"):
        st.write(user_ip)
    st.session_state.messages.append({"role":"user","msg":user_ip})
    config = {"configurable":{"thread_id":thread_id}}

    for chat in st.session_state["messages"]:
        if chat["role"] == "user":
            lc_message.append(HumanMessage(content=chat["msg"]))
        else:
            lc_message.append(AIMessage(content=chat["msg"]))



    message = {"messages":lc_message}
    response = chatbot.invoke(message,config)#config adds the current message to the history because of the config passed 
    st.session_state.messages.append({"role":"assistant","msg":response["messages"][-1].content})
    with st.chat_message("assistant"):
        st.write(response["messages"][-1].content)