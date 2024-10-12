'''
1. Bag of Words
- 단어들의 순서는 고려하지 않고, 출현빈도(frequency)만 고려하는 텍스트 데이터의 수치화 표현방법
    - 단어의 수가 많은 경우 비효율적임 (큰메모리, 높은 계산 복잡도)
    - DTM의 대부분이 0으로 표현됨
    - 단어들이 나타나는 순서가 무시됨 -> 문맥 정보를 파악하기 어려움
    - 문서간의 연관성을 표현하는데 제한이 있음
- 사이킷런 CountVectorizer : 문서 내에 있는 단어수를 count해서 vector로 만들어주는 모듈 (문서단어행렬_DTM)
'''
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

doc1 = '먹고 싶은 사과'
doc2 = '먹고 싶은 바나나'
doc3 = '길고 노란 바나나 바나나'
doc4 = '저는 과일이 좋아요'

docs = [doc1, doc2, doc3, doc4]

# CountVectorizer 객체 생성
countVectorizer = CountVectorizer()

# 문서를 BoW 행렬로 변환
bow_matrix = countVectorizer.fit_transform(docs)

# BoW 행렬을 array로 저장
bow_scores = bow_matrix.toarray()

# 특성 이름(단어) 가져오기
feature_names = countVectorizer.get_feature_names_out()

# 결과를 표시하기 위한 pandas DataFrame 생성
dataframe_bow = pd.DataFrame(bow_scores, columns = feature_names)

# 문서 텍스트를 담은 컬럼 추가
dataframe_bow['문서'] = docs

bow_scores

dataframe_bow