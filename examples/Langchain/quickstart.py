from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatOpenAI(openai_api_key=api_key) # type: ignore

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 사회부 기자입니다. 제목, 서론, 본론, 결론으로 기사를 작성하시오"),
        ("user", "{input}")
    ]
)

chain = prompt | llm
for chunk in chain.stream({"input": "지구 온난하 위기에 대해 설명해줘"}):
    print(chunk.content, end="", flush=True)


