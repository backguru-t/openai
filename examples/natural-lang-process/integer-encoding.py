from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

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

vocab_dict = {}
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
                if word not in vocab_dict:
                    vocab_dict[word] = 0 
                vocab_dict[word] += 1
    preprocessed_sentences.append(result) 
print(preprocessed_sentences)
print("\n")
print("단어빈도수 (단어:빈도수): ", vocab_dict)

vocab_dict_sorted = sorted(vocab_dict.items(), key=lambda x : x[1], reverse=True)
print("단어빈도수 내림차순 정렬:", vocab_dict_sorted)

# 높은 빈도수를 가진 단어일수록 낮은 정수를 부여하며 정수는 1부터 시작함
word_to_index = {}
i = 0
for (word, frequency) in vocab_dict_sorted:
    if frequency > 1:   # 빈도수가 1인 단어는 제외
        i += 1
        word_to_index[word] = i
print("정수 인코딩 (빈도수 1인 단어 제거): ", word_to_index)

#  상위 5개 단어만 사용할 경우 나머지는 제거
vocab_size = 5
words_frequency = [word for word, index in word_to_index.items() if index >= vocab_size + 1]
for w in words_frequency:
    del word_to_index[w]

print("상위 5개만 사용: ", word_to_index)

# Out-Of-Vocabulary 처리
word_to_index["OOV"] = len(word_to_index) + 1
print("OOV added:", word_to_index)

# 앞 문장애서 추출된 정제된 단어들을 정수 인코딩
encoded_sentences = []
for sentence in preprocessed_sentences:
    encoded_sentence = []
    for word in sentence:
        try:
            encoded_sentence.append(word_to_index[word])
        except KeyError:
            encoded_sentence.append(word_to_index["OOV"])
    encoded_sentences.append(encoded_sentence)
print("정수인코딩: ", encoded_sentences)