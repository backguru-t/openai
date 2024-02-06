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