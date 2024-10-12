'''
1. Bag of Words(BoW)
- 각 단어에 고유한 정수 인덱스 부여 -> 벡터 생성 -> 각 단어 등장횟수 기록
- 문서에 포함된 단어의 빈도를 벡터 형태로 표출 (build_bag_of_words 함수)
'''
from nltk.tokenize import TreebankWordTokenizer

def build_bag_of_words(doc):
    
    # 온점 제거 및 토큰화 진행
    doc = doc.replace('.', '')
    tokenized_document = TreebankWordTokenizer().tokenize(doc)
    
    # 단어 <-> 인덱스 매핑 딕셔너리
    word_to_index = {}
    
    # BoW를 저장할 리스트 (단어 빈도)
    bow = []
    
    for word in tokenized_document:
        
        # 단어가 처음 등장 -> 인덱스 부여, BoW에 1 추가
        if word not in word_to_index.keys():
            word_to_index[word] = len(word_to_index)
            bow.insert(len(word_to_index) -1, 1)
        
        # 이미 등장한 단어 -> 해당 인덱스 위치의 BoW 값에 1 추가
        else:
            index = word_to_index.get(word)
            bow[index] = bow[index] + 1
    
    return word_to_index, bow

doc1 = "Imagination is more important than knowledge"

vocab, bow = build_bag_of_words(doc1)

print('vocabulary : ', vocab)
print('bag of words vector : ', bow)

doc2 = "Knowledge is limited"

vocab, bow = build_bag_of_words(doc2)

print('vocabulary : ', vocab)
print('bag of words vector : ', bow)

doc3 = "Imagenation encircles the world"

vocab, bow = build_bag_of_words(doc3)

print('vocabulary : ', vocab)
print('bag of words vector : ', bow)

doc4 = doc1 + " " + doc2 + " " + doc3

vocab, bow = build_bag_of_words(doc4)

print('vocabulary : ', vocab)
print('bag of words vector : ', bow)


'''
2. TF-IDF (단어빈도-역문서빈도)
- 특정 문서 내에서 단어 빈도가 높을수록 : 중요도 증가
- 전체 문서들에서는 그 단어를 포함한 문서가 적을수록(흔하지 않을수록) : 점수 증가
-> 모든 문서에 나타나는 흔한 단어의 중요도를 낮게 두는 방식
'''
import pandas as pd
from math import log

doc1 = '먹고 싶은 사과'
doc2 = '먹고 싶은 바나나'
doc3 = '길고 노란 바나나 바나나'
doc4 = '저는 과일이 좋아요'

docs = [doc1, doc2, doc3, doc4]

# 총 문서의 수
D = len(docs)

# 문서 d 내에서(특정문서) 단어 t의 빈도(TF) 계산
def tf(t, d):
    return d.count(t)

# 단어 t의 역문서 빈도(IDF) 계산
def idf(t):
    df = 0
    
    for doc in docs:
        # doc에 t가 있는지 확인
        df += t in doc
    return log(D/(df+1))
    # return log((D+1)/(df+1)) + 1

# TF-IDF 점수 계산
def tfidf(t, d):
    return tf(t, d) * idf(t)

# 문서 내에 등장하는 단어의 집합
vocas = list(set(w for doc in docs for w in doc.split()))
vocas.sort()

vocas

result = []

for doc in docs:
    result.append([])
    
    for voca in vocas:
        result[-1].append(tf(voca, doc))

tf_score = pd.DataFrame(result, columns=vocas)

tf_score

result = []

for voca in vocas:
    result.append(idf(voca))
    
idf_score = pd.DataFrame(result, index=vocas, columns=["IDF"])

idf_score

result = []

for doc in docs:
    result.append([])
    
    for voca in vocas:
        result[-1].append(tfidf(voca, doc))
        
        
tfidf_score = pd.DataFrame(result, columns=vocas)

tfidf_score