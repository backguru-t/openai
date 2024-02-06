from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

prompt = ChatPromptTemplate.from_template(
    "내게 {topic}에 관해서 재미있는 농담을 해줘"
)
output_parser = StrOutputParser()
model = ChatOpenAI(openai_api_key=api_key)
chain = (
    {"topic": RunnablePassthrough()} 
    | prompt
    | model
    | output_parser
)

print(chain.invoke("자전거"))