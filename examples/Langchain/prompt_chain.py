from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

prompt = ChatPromptTemplate.from_template("내게 {topic}에 관해서 재미있는 농담을 해줘")
model = ChatOpenAI(openai_api_key=api_key) # type: ignore
output_parser = StrOutputParser()

chain = prompt | model |output_parser

chain.invoke({"topic":"커피"})