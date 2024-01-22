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
# print(chain.invoke({"input": "전세사기 관련해서 이야기해줘"}))

loader = WebBaseLoader("https://n.news.naver.com/article/119/0002758949")

docs = loader.load()
# print(docs)

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

response = retrieval_chain.invoke({"input": "다음 내용을 제목, 서론, 본론, 결론으로 요약해줘"})
print(response["answer"])