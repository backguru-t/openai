# 단어 집합(vocabulary)은 앞으로 자연어 처리에서 계속 나오는 개념이다.
# 단어 집합은 서로 다른 단어들의 집합입니다. 여기서 서로 다른 단어라는 것은 기본적으로 
# book과 books와 같이 단어의 변형 형태도 다른 단어로 간주하는 것을 의미한다. 
# 원-핫 인코딩이란 단어 집합에 있는 단어들을 가지고, 문자를 숫자, 더 구체적으로는 벡터로 바꾸는 
# 기법을 의미한다.
# 케라스는 원-핫 인코딩을 수행하는 유용한 도구 to_categorical()를 지원

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

text = "나랑 점심 먹으러 갈래 점심 메뉴는 햄버거 갈래 갈래 햄버거 최고야"

tokenizer = Tokenizer()
# 빈도수가 높은 단어일 수록 낮은 인덱스를 부여
tokenizer.fit_on_texts([text])
print("단어 빈도수: ", tokenizer.word_counts)
print("단어 집합: ", tokenizer.word_index)

sub_text = "점심 먹으러 갈래 메뉴는 햄버거 최고야"
encoded = tokenizer.texts_to_sequences([sub_text])[0]
print(encoded)

# 원-핫 인코딩
one_hot = to_categorical(encoded)
print(one_hot)