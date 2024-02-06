from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatOpenAI(openai_api_key=api_key) # type: ignore

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 사회부 기자입니다. 100자 이내로 기사를 작성하시오"),
        ("user", "{input}")
    ]
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser
# for chunk in chain.stream({"input": "지구 온난하 위기에 대해 설명해줘"}):
#     print(chunk.content, end="", flush=True)

questions = [
    {"input":"한국에 TOP5에 들어가는 음식은 무었인가요?"},
    {"input":"한국 수도 서울에서 가장 유명한 장소 1곳은 어디인가요?"},
    {"input":"한국에서 가장 유명한 축구선수는 누구인가요?"},
]

print(chain.batch(questions))