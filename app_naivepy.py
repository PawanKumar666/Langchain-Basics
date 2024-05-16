import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a flirty girl, you should answer all the questions in a flirty tone"),
        ("user", "{question}")
    ]
)
 
input_text = input("Ask anything, he is a bot, type exit to exit\n")

# Define openai llm
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

while input_text != "exit":
    print(chain.invoke({"question": input_text}))
    input_text = input("\n")

