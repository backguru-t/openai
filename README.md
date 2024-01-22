# OpenAI Examples

**Table of contents**
- [서론](#서론)
- [Trouble Shootings](#Trouble-shootings)
- [자연어 처리를 위한 패키지 설치](#자연어-처리를-위한-패키지-설치)
- [텍스트 전처리 과정 1. 토큰화](#텍스트-토큰화)
- [텍스트 전처리 과정 2. 정제](#텍스트-정제)
- [텍스트 전처리 과정 3. 정규화](#텍스트-정규화)

## 서론
여기서 제공되는 예제와 가이드는 [Open API](https://platform.openai.com/docs/api-reference) 와 [Documentation](https://platform.openai.com/docs/introduction)을 준수한다. 예제를 실행하기 위해서는 API KEY가 필요하며 head honcho에게 문의바란다. 또한 개발 환경은 아래와 같이 여러 가지 방법으로 구성이 가능하다.

### 내 노트북에서 개발하기
파이썬(3.11.5 사용됨)을 직접 다운 받아 설치한 후 다음과 같이 가상환경을 구성하여 개발이 가능하다. 물론 가상 환경을 구성하지 않아도 된다. 하지만 버전에 따른 호환성 등을 고려한다면 가상환경을 생성 해서 사용하는 것을 추천한다. 가상환경(virtualenv)은 여러 개의 파이썬 프로젝트가 하나의 컴퓨터에서 충동을 일으키지 않고 존재할 수 있도록 해준다. virtualenv는 각 프로그램별로 완전히 독립적인 가상의 환경을 만들어서 각 프로그램별로 라이브러리 모듈등의 버전을 별도로 지정할 수 있게 한다. 즉 한 컴퓨터에 여러 개발환경을 서로 독립적으로 설치, 실행할 수 있는 것과 동일하다.

```bash
python -m venv 가상환경이름
```

필요한 모듈을 일일이 설치해야 하는 단점이 있지만 설치가 필요한 모듈을 requrements.txt를 통해 제공하므로 아래 명령으로 한번에 모듈 설치가 가능하다.

```bash
pip install -r requirements.txt
```

### Anaconda 사용하기
[아나콘다](https://www.anaconda.com/)를 사용하면 대부분의 패키지가 설치되어 있으니 파이썬 배포판 아나콘다를 이용하는 것도 좋은 방법이다. 아나콘다를 이용해도 가상환경을 생성하여 개발하는 것을 추천한다.

### 구글의 Colab 사용하기
인터넷만 된다면 바로 파이썬을 개발할 수 있는 [코랩](https://colab.research.google.com/)을 사용할 수 있다. 특히 딥 러닝에서는 CPU보다는 GPU를 많이 사용하는 데 코랩을 사용하면 GPU를 무료로 사용할 수 있다.

## Trouble shootings
- *ERROR: Could not build wheels for multidict*: install the latest Microsoft Visual C++ build tools 

Wishing you good luck.

## 자연어 처리를 위한 패키지 설치
자연어 (NL)란 우리가 일상 생활에서 사용하는 언어를 의미하며, 자연어 처리 (NLP)란 이런 자연어의 의미를 분석하여 컴퓨터가 처리할 수 있도록 하는 일을 의미하며, 챗봇, 감성 분석 및 뉴스 기사 분류 등과 같은 분야에서 이용 되고 있다.

### 텐서 플로우 설치
파이썬 버전과 테스트된 빌드는 [다음 표](https://www.tensorflow.org/install/source?hl=ko#tested_build_configurations)를 참고한다. 아래와 같이 설치를 진행한다.

```bash
pip install tensorflow
```
### 케라스 설치
Keras는 딥 러닝 프레임워크인 텐서 플로우에 대한 추상화 된 API를 제공한다. 앞서 텐서플러우를 설치하면 함께 설치 된다.

```bash
pip install keras
```

### Gensim 설치
젠심은 머신 러닝을 사용하여 토픽 모델링과 자연어처리 등을 수행할 수 있게 해주는 오픈 소스 라이브러리이다.

```bash
pip install gensim
```
### 사이킷런
Scikit-learn은 파이썬 머신러닝 라이브러리이다. 사이킷런에는 머신러닝을 연습하기 위한 아이리스 데이터, 당뇨병 데이터 등 자체 데이터를 포함하고 있다.

```bash
pip install scikit-learn
```

### NLTK 설치
텍스트 전처리를 위한 패키지를 설치한다.

```bash
pip install nltk
```
그리고, 파이썬 쉘에서 다음 코드를 입력하여 NLTK 데이터를 모두 다운로드 받는다.

```bash
import nltk
nltk.download()
```

### KoNLPy 설치
한국어 자연어 처리를 위해 아래와 같이 설치한다.

```bash
pip install konlpy
```

추가적으로 아래와 같이 데이터 분석을 위한 패키지를 설치한다.

```bash
pip install pandas numpy matplotlib
```

## 텍스트 토큰화
Corpus 데이터는 training 자료로 사용되지 전에 토큰화-정제-정규화 과정이라는 전처리 과정을 거친다. 

### Word tokenization

### Setence tokenization


## 텍스트 정제

## 텍스트 정규화