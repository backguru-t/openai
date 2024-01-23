# 단어 집합(vocabulary)은 앞으로 자연어 처리에서 계속 나오는 개념이다.
# 단어 집합은 서로 다른 단어들의 집합입니다. 여기서 서로 다른 단어라는 것은 기본적으로 
# book과 books와 같이 단어의 변형 형태도 다른 단어로 간주하는 것을 의미한다. 
# 원-핫 인코딩이란 단어 집합에 있는 단어들을 가지고, 문자를 숫자, 더 구체적으로는 벡터로 바꾸는 
# 기법을 의미한다.

from konlpy.tag import Okt  

# Okt 형태소 분석기를 통해서 문장에 대해서 토큰화를 수행
okt = Okt()  
tokens = okt.morphs("나는 자연어 처리를 배운다")  
print(tokens)

# 각 토큰에 대해서 고유한 정수를 부여
word_to_index = {word : index for index, word in enumerate(tokens)}
print("단어 집합: ", word_to_index)

def one_hot_encoding(word, word_to_index):
    one_hot_vector = [0]*(len(word_to_index))
    index = word_to_index[word]
    one_hot_vector[index] = 1
    return one_hot_vector

# '자연어'라는 단어의 원-핫 벡터
# '자연어'는 정수 2이므로 원-핫 벡터는 인덱스 2의 값이 1이며, 나머지 값은 0인 벡터가 나옴
print(one_hot_encoding("자연어", word_to_index))