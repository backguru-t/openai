from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer

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

vocab_size = 5

# 기본 사용
# tokenizer = Tokenizer()

# 상위 5개만 사용할 경우
# tokenizer = Tokenizer(num_words = vocab_size + 1)

# 케라스 토크나이저는 기본적으로 단어 집합에 없는 단어인 OOV에 대해서는 단어를 정수로 
# 바꾸는 과정에서 아예 단어를 제거한다는 특징이 있음. 단어 집합에 없는 단어들은 OOV로 
# 간주하여 보존하고 싶다면 Tokenizer의 인자 oov_token을 사용함
# keras는 기본적으로 OOV를 1로 지정함
tokenizer = Tokenizer(num_words = vocab_size + 2, oov_token = "OOV")

# fit_on_texts는 입력한 텍스트로부터 단어 빈도수가 높은 순으로 낮은 정수 인덱스를 부여
tokenizer.fit_on_texts(preprocessed_sentences)

print(tokenizer.word_index)
print("\n")
print(tokenizer.word_counts)

# texts_to_sequences()는 입력으로 들어온 코퍼스에 대해서 각 단어를 이미 정해진 인덱스로 변환
print(tokenizer.texts_to_sequences(preprocessed_sentences))
