import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "keywhichfails")

# For Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "keywhichfails")

# Form Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a bot, provide irrelevant response to user queries, your responses shouldn't relate with what the user asked, it should be the opposite"),
        ("user", "Question:{question}")
    ]
)

# Defining streamlit 

st.title("Langchain irrelevant response generator")
input_text = st.text_input("Ask anything, he is a bot")

# Define openai llm
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser() # Used to parse
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))