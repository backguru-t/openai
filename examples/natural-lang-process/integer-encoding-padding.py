from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np

raw_text = """
A barber is a person. a barber is good person. 
a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. 
Huge secret. His barber kept his word. a barber kept his word. 
His barber kept his secret. But keeping and keeping such a huge secret to himself
was driving the barber crazy. the barber went up a huge mountain.
"""

# sentence tokenization
sentences = sent_tokenize(raw_text)
# print(sentences)

# cleaning and normalization
# 단어를 소문자로 변경하고 불용어와 단어 길이가 2이하인 경우에 대해 일부 단어 제거
# 텍스트를 수치화 한다는 의미는 본격적으로 자연어 처리 작업을 시작한다는 의미이므로
# 최대한의 전처리 작업을 진행해 놓아야 함

preprocessed_sentences = []
stop_words = set(stopwords.words('english'))

for sentence in sentences:
    # 단어 토큰화
    tokenized_sentence = word_tokenize(sentence)
    result = []

    for word in tokenized_sentence: 
        word = word.lower() # 모든 단어를 소문자화하여 단어의 개수를 줄인다.
        if word not in stop_words: # 단어 토큰화 된 결과에 대해서 불용어를 제거한다.
            if len(word) > 2: # 단어 길이가 2이하인 경우에 대하여 추가로 단어를 제거한다.
                result.append(word)

    preprocessed_sentences.append(result) 
print(preprocessed_sentences)
print("\n")

# 기본 사용
tokenizer = Tokenizer()

# fit_on_texts는 입력한 텍스트로부터 단어 빈도수가 높은 순으로 낮은 정수 인덱스를 부여
tokenizer.fit_on_texts(preprocessed_sentences)

print(tokenizer.word_counts)
print("\n")
print(tokenizer.word_index)

encoded = tokenizer.texts_to_sequences(preprocessed_sentences)
print(encoded)

# 모두 동일한 길이로 맞춰주기 위해서 이 중에서 가장 길이가 긴 문장의 길이를 계산
max_len = max(len(item) for item in encoded)
print("최대길이: ", max_len)

for sentence in encoded:
    while len(sentence) < max_len:
        sentence.append(0)

padded_up = np.array(encoded)
# 이제 이들을 하나의 행렬로 보고 병렬 처리를 할 수 있음
# 이와 같이 데이터에 특정 값을 채워서 데이터의 크기를 조정하는 것을 padding이라고 하며
# 숫자 0을 넣어서 zero padding이라고 함
print(padded_up)

