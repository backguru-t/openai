from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter


load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatOpenAI(openai_api_key=api_key) # type: ignore

# for chunk in llm.stream("List the U.S. Presidents in chronological order"):
#     print(chunk.content, end="", flush=True)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 사회 분야 기자입니다."),
        ("user", "{input}")
    ]
)

chain = prompt | llm

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

test_news_url = "https://n.news.naver.com/mnews/article/092/0002321211"
loader = WebBaseLoader(test_news_url)

docs = loader.load()
print(docs)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
documents = text_splitter.split_documents(docs)
print (f"You have {len(documents)} documents")

embeddings = OpenAIEmbeddings(openai_api_key=api_key)
vector = FAISS.from_documents(documents, embeddings)

from langchain.chains.combine_documents import create_stuff_documents_chain

prompt = ChatPromptTemplate.from_template("""다음과 같이 제공되는 내용을 기반으로 질문에 답해줘:

<context>
{context}
</context>

Question: {input}""")

print(prompt)
document_chain = create_stuff_documents_chain(llm, prompt)

from langchain.chains import create_retrieval_chain

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "본문의 내용을 5~7문장으로 제목, 서론, 본론, 결론으로 나누어 요약해줘"})
print(response["answer"])