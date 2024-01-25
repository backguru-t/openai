# OpenAI Examples

여기서 제공되는 예제와 가이드는 [Open API](https://platform.openai.com/docs/api-reference) 와 [Documentation](https://platform.openai.com/docs/introduction)을 준수한다. 예제를 실행하기 위해서는 API KEY가 필요하며 head honcho에게 문의바란다. 또한 개발 환경은 아래와 같이 여러 가지 방법으로 구성이 가능하다.

## 내 노트북에서 개발하기
파이썬(3.11.5 사용됨)을 직접 다운 받아 설치한 후 다음과 같이 가상환경을 구성하여 개발이 가능하다. 물론 가상 환경을 구성하지 않아도 된다. 하지만 버전에 따른 호환성 등을 고려한다면 가상환경을 생성 해서 사용하는 것을 추천한다. 가상환경(virtualenv)은 여러 개의 파이썬 프로젝트가 하나의 컴퓨터에서 충동을 일으키지 않고 존재할 수 있도록 해준다. virtualenv는 각 프로그램별로 완전히 독립적인 가상의 환경을 만들어서 각 프로그램별로 라이브러리 모듈등의 버전을 별도로 지정할 수 있게 한다. 즉 한 컴퓨터에 여러 개발환경을 서로 독립적으로 설치, 실행할 수 있는 것과 동일하다.

```bash
python -m venv 가상환경이름
```

필요한 모듈을 일일이 설치해야 하는 단점이 있지만 설치가 필요한 모듈을 requrements.txt를 통해 제공하므로 아래 명령으로 한번에 모듈 설치가 가능하다.

```bash
pip install -r requirements.txt
```

## Anaconda 사용하기
[아나콘다](https://www.anaconda.com/)를 사용하면 대부분의 패키지가 설치되어 있으니 파이썬 배포판 아나콘다를 이용하는 것도 좋은 방법이다. 아나콘다를 이용해도 가상환경을 생성하여 개발하는 것을 추천한다.

## 구글의 Colab 사용하기
인터넷만 된다면 바로 파이썬을 개발할 수 있는 [코랩](https://colab.research.google.com/)을 사용할 수 있다. 특히 딥 러닝에서는 CPU보다는 GPU를 많이 사용하는 데 코랩을 사용하면 GPU를 무료로 사용할 수 있다.

## Trouble shootings
- *ERROR: Could not build wheels for multidict*: install the latest Microsoft Visual C++ build tools 

Wishing you good luck.

