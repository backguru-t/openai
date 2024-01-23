from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatOpenAI(openai_api_key=api_key) # type: ignore

# for chunk in llm.stream("List the U.S. Presidents in chronological order"):
#     print(chunk.content, end="", flush=True)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are world class journalist."),
        ("user", "{input}")
    ]
)

chain = prompt | llm
print(chain.invoke({"input": "explain global climate change"}).content)



