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


'''
2. TF-IDF
- 특정 문서 내에서 단어 빈도가 높을수록 : 중요도 증가
- 전체 문서들에서는 그 단어를 포함한 문서가 적을수록(흔하지 않을수록) : 점수 증가
-> 모든 문서에 나타나는 흔한 단어의 중요도를 낮게 두는 방식
'''
from sklearn.feature_extraction.text import TfidfVectorizer

# TfidfVectorizer 초기화
tfidfVectorizer = TfidfVectorizer()

# 문서를 Tf-IDF 행렬로 변환
tfidf_matrix = tfidfVectorizer.fit_transform(docs)

# TF-IDF 행렬을 array로 저장
tfidf_scores = tfidf_matrix.toarray()

# 특성이름(단어) 가져오기
feature_names = tfidfVectorizer.get_feature_names_out()

# DataFrame 생성
dataframe_tfidf = pd.DataFrame(tfidf_scores, columns=feature_names)

dataframe_tfidf['문서'] = docs

tfidf_scores

dataframe_tfidf


'''
3. 코사인 유사도
- 두 벡터 간의 코사인 각도를 이용하여 구하는 두 벡터의 유사도
- 코사인유사도 : -1 (180도 방향)
- 코사인유사도 : 0 (90도 방향)
- 코사인유사도 : 1 (0도 방향)
'''
from sklearn.metrics.pairwise import cosine_similarity

# 모든 문서(BoW) 사이의 코사인 유사도 개선
cosine_similarities = cosine_similarity(bow_matrix)

# 코사인 유사도 행렬 출력
dataframe_cosine_similarities = pd.DataFrame(cosine_similarities, columns=docs, index=docs)

dataframe_cosine_similarities