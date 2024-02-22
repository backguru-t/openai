# LangChain guide

## Langchain OpenAI integration package 설치

```bash
pip install langchain-openai
```

OpenAI key를 아래와 같이 파라미터로 전달하여 OpenAI LLM을 초기화 한다.

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_key="...")
```

또는 .env파일을 생성하여 API_KEY를 선언한 후 아래와 같이 호출하여 사용 가능하다.

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatOpenAI(openai_api_key=api_key)
```

## LangChain Expression Language
아래 코드는 UNIX 파이프라인과 동작이 유사한 chaining 표현을 나타낸다. 즉, prompt 생성 후 model의 입력으로 전달되고 model의 출력이 output parser로 전달된다.

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI(model="gpt-4")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

chain.invoke({"topic": "ice cream"})
```

## Stream
메세지를 stream 형식을 출력하기 위해 아래 코드와 같이 `invoke`함수 대신 `stream` 함수를 사용한다.

```python
for chunk in chain.stream("ice cream"):
    print(chunk, end="", flush=True)
```

## Batch
한번에 여러 개의 입력을 받아 처리할 수 있는 배치 방식을 사용할 수 있다.

```python
questions = [
    {"input":"한국에 TOP5에 들어가는 음식은 무었인가요?"},
    {"input":"한국 수도 서울에서 가장 유명한 장소 1곳은 어디인가요?"},
    {"input":"한국에서 가장 유명한 축구선수는 누구인가요?"},
]

chain.batch(questions)
```

## Interface
Langchain은 아래와 같이 3가지 타입의 인터페이스와 별개의 async 방식을 지원한다.

- `stream`: stream back chunks of the response
- `invoke`: call the chain on an input
- `batch`: call the chain on a list of inputs

- `astream`: stream back chunks of the response async
- `ainvoke`: call the chain on an input async
- `abatch`: call the chain on a list of inputs async

## RAG architecture
- `Load`: 데이터를 [DocumentLoaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)를 이용하여 로드하는 작업
- `Split`: [Text SPlitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/)를 이용하여 대량의 document를 작은 chunk 단위로 쪼개는 작업
- `Store`: chunk단위로 조각난 데이터를 저장하고 인덱싱하는 작업으로 [Embedding](https://python.langchain.com/docs/modules/data_connection/text_embedding/) 모델을 이용해서 vector data를 생성하고 [VectorStore](https://python.langchain.com/docs/modules/data_connection/vectorstores/)에 저장

![img](images/retrieval-step.png)

- `Retrieve`: 사용자의 질의가 있을대 [Retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/)를 이용하여 위에서 생성한 저장소에서 연관데이터를 검색하고 가져오는 작업
- `Generate`: LLM이 사용자의 질문과 연관된 데이터를 수집하여 prompt를 생성하고 그에 상응하는 대답을 생성 하는 작업

### Document loaders
https://python.langchain.com/docs/modules/data_connection/document_loaders/

### Text splitters
https://python.langchain.com/docs/modules/data_connection/document_transformers/

### Embedding models
https://python.langchain.com/docs/modules/data_connection/text_embedding/

```python
from langchain_openai import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(openai_api_key="...")

embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
len(embeddings), len(embeddings[0])
```

### Vector stores
https://python.langchain.com/docs/modules/data_connection/vectorstores/

### Retrievers
https://python.langchain.com/docs/modules/data_connection/retrievers/

### Indexing
https://python.langchain.com/docs/modules/data_connection/indexing

## RAG with semi-structured data 샘플 코드
비정형 데이터를 embedding하기 위해 text splitting을 하다 보면 테이블이 깨지며 그로 인해 그 테이블에서 유의미한 데이터를 유실하게 된다. 따라서 여기서 제시되는 샘플 코드에서는 다음의 기법을 활용하여 해당 문제점을 극복한다.

- [Unstructured](https://unstructured.io/) 사용하여 텍스트와 테이블을 파싱
- [MultiVector Retriver](https://python.langchain.com/docs/modules/data_connection/retrievers/multi_vector)를 사용하여 테이블과 텍스트 저장
- [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) OCR 엔진
- [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) pdf rendering

> Tesseract와 Poppler 설치 후 tesseract 설치 폴더와 poppler의 bin 폴더를 시스템 PATH에 추가해 주어야 한다.

해당 샘플 코드에서는 pdf 파일을 다루기 위해 Unstructured의 [partion_pdf](https://unstructured-io.github.io/unstructured/core/partition.html#partition-pdf)를 사용한다.



