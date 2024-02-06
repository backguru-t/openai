from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

prompt = ChatPromptTemplate.from_template("{topic}에 관해 한국에서 가장 유명한 것이 무었인지, 100자 내외로 설명해줘")
model = ChatOpenAI(openai_api_key=api_key) # type: ignore

chain = prompt | model | StrOutputParser()

print(chain.invoke({"topic":"음식"}))