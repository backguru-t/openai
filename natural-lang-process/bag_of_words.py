# 각 단어에 고유한 정수 인덱스를 부여합니다. (단어 집합 생성)
# 각 인덱스의 위치에 단어 토큰의 등장 횟수를 기록한 벡터를 만듭니다.  
# BoW는 각 단어가 등장한 횟수를 수치화하는 텍스트 표현 방법이므로 주로 어떤 단어가 
# 얼마나 등장했는지를 기준으로 문서가 어떤 성격의 문서인지를 판단하는 작업에 쓰인다. 
# 즉, 분류 문제나 여러 문서 간의 유사도를 구하는 문제에 주로 쓰인다. 가령, '달리기', 
# '체력', '근력'과 같은 단어가 자주 등장하면 해당 문서를 체육 관련 문서로 분류할 수 있을
# 것이며, '미분', '방정식', '부등식'과 같은 단어가 자주 등장한다면 수학 관련 문서로 
# 분류할 수 있을 것이다.

from konlpy.tag import Okt

okt = Okt()

def build_bag_of_words(document):
    document = document.replace('.', '')
    tokenized_document = okt.morphs(document)

    word_to_index = {}
    bow = []

    for word in tokenized_document:  
        if word not in word_to_index.keys():
            word_to_index[word] = len(word_to_index)  
            # BoW에 전부 기본값 1을 넣는다.
            bow.insert(len(word_to_index) - 1, 1)
        else:
            # 재등장하는 단어의 인덱스
            index = word_to_index.get(word)
            # 재등장한 단어는 해당하는 인덱스의 위치에 1을 더한다.
            bow[index] = bow[index] + 1

    return word_to_index, bow

doc1 = "정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다."
vocab, bow = build_bag_of_words(doc1)
print('vocabulary :', vocab)
print('bag of words vector :', bow)
