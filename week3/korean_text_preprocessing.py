'''
0. KoNLPy(Korean NLP in Python 설치)
- 한국어 자연어처리를 위한 파이썬 패키지
'''
# 터미널 -> pip install konlpy
import nltk
nltk.download('punkt')

'''
1. 토큰화(Tokenization)
'''
'''
1-1. 단어토큰화
- KoNLPy에서 제공하는 형태소 분석기 : Okt(Open Korea Text), Mecab(메캅), Komoran(코모란), Hannanum(한나눔), 꼬꼬마(Kkma)
- KoNLPy 형태소 분석기 공통 메서드 : morphs(토큰화), pos(품사태깅), nouns(명사추출)
'''
# Okt(Open Korea Text)
from konlpy.tag import Okt
# Komoran(코모란)
from konlpy.tag import Komoran
# Hannanum(한나눔)
from konlpy.tag import Hannanum
# 꼬꼬마(Kkma)
from konlpy.tag import Kkma

# 객체생성
okt = Okt()
komoran = Komoran()
hannanum = Hannanum()
kkma = Kkma()

text = "세종대왕은 온 백성이 자유롭게 자신의 의사를 표현하고 정보를 얻을 수 있는 세상을 꿈꾸며 한글을 창제하였습니다"

# morphs : 토큰화 메서드
print("Okt : ", okt.morphs(text))
print("Komoran : ", komoran.morphs(text))
print("Hannanum : ", hannanum.morphs(text))
print("Kkma : ", kkma.morphs(text))

'''
1-2. 문장토큰화
'''
# 문장 토크나이저
from nltk.tokenize import sent_tokenize

para_kor = """세종대왕은 온 백성이 자유롭게 자신의 의사를 표현하고 정보를 얻을 수 있는 세상을 꿈꾸며 ‘한글’을 창제하였습니다.
국립국어원은 그 꿈을 이어가는 중추적인 기관으로서 사명을 다할 것입니다.
한국어와 한글이, 남과 북을 넘어 온 세상 사람들이 소통하는 도구가 되어 우리의 삶을 더욱 풍성하게 하는 데에 힘을 보태겠습니다."""

# 문장 단위로 텍스트 분할
sent_tokenize(para_kor)

'''
2. 불용어 제거
'''
text = "세종대왕은 온 백성이 자유롭게 자신의 의사를 표현하고 정보를 얻을 수 있는 세상을 꿈꾸며 한글을 창제하였습니다"
stop_words = "은 이 의 을 를 하고 있는 하였습니다"

# 불용어 문자열을 공백 기준으로 나눠서 집합으로 변환
stop_words = set(stop_words.split(' '))

# 단어 토큰화
word_tokens = okt.morphs(text)

# 토큰화된 텍스트에서 불용어 제거
result = [word for word in word_tokens if not word in stop_words]

print('불용어 제거 전 : ', word_tokens)
print('불용어 제거 후 : ', result)

# 불용어 사전 파일
stop_words_file = open("/Users/sunyeonjeong/dev/github/textMining/week3/korean_stopwords.txt", "r")
stop_words_text = stop_words_file.read()
stop_words_text

stop_words_set = set(stop_words_text.split('\n'))
stop_words_set

result = [word for word in word_tokens if not word in stop_words_set]

print("불용어 제거 전 : ", word_tokens)
print("불용어 제거 후 : ", result)

'''
3. 품사태깅
'''
# 객체생성
okt = Okt()
komoran = Komoran()
hannanum = Hannanum()
kkma = Kkma()

text = "세종대왕은 온 백성이 자유롭게 자신의 의사를 표현하고 정보를 얻을 수 있는 세상을 꿈꾸며 한글을 창제하였습니다"

# 토큰화 결과와 함께 각 토큰마다 해당하는 품사 태그가 붙음
print(okt.pos(text))
print(komoran.pos(text))
print(hannanum.pos(text))
print(kkma.pos(text))

# 토큰화 결과에서 명사만 추출
print(okt.nouns(text))
print(komoran.nouns(text))
print(hannanum.nouns(text))
print(kkma.nouns(text))

'''
4. 문서 탐색 : 문서 내의 문자/토큰 수, 빈도 수 높은 단어 탐색
(https://konlpy.org/en/latest/examples/explore/)
'''
# 빈도 계산 모듈
from collections import Counter

# konlpy 라이브러리
from konlpy.corpus import kolaw
from konlpy.tag import Hannanum
from konlpy.utils import concordance, pprint
from matplotlib import pyplot

# 대한민국 헌법 텍스트파일 (constitution.txt) 파일읽기
doc = kolaw.open('constitution.txt').read()

# Hannanum 형태소 분석기 -> 품사태깅
pos = Hannanum().pos(doc)

# 품사 태깅 된 결과 빈도 계산
cnt = Counter(pos)

# 텍스트 문자 수, 단어 수 (띄어쓰기 기준), 품사 태깅 집합
print('nchars : ', len(doc))
print('ntokens : ', len(doc.split()))
print('nmorphs : ', len(set(pos)))

# 가장 빈도가 높은 상위 20개의 형태소
print('\nTop 20 frequent morphemes : ')
pprint(cnt.most_common(20)) # pprint : 데이터를 이쁘게 출력

# "대한민국"이 텍스트 내에서 나타나는 위치 출력
'''
- concordance : 특정 단어가 문서에서 등장하는 위치를 찾는 함수
- u'대한민국' : 검색할 단어를 유니코드 문자열로 지정
- show=True : 결과를 출력하라는 옵션
'''
print('\nLocations of "대한민국" in the document : ')
concordance(u'대한민국', doc, show=True)

'''
5. 연속된 단어 찾기 (collocation)
- 한국어 단어의 연관성 분석을 위해 NLTK의 'colloctions'을 사용해 연속된 단어를 찾음
'''
from konlpy.tag import Kkma
from konlpy.corpus import kolaw
from konlpy.utils import pprint
from nltk import collocations

# colloction 방법 선택
# - measures = collocations.BigramAssocMeasures() : bi-gram
# - measures = colloctions.TrigramAssocMeasures() : Tri-gram
measures = collocations.QuadgramAssocMeasures() # 연속된 4개의 단어조합

doc = kolaw.open('constitution.txt').read()

# Kkma 형태소 분석기 사용을 통한 품사태깅
tagged_words = Kkma().pos(doc)

# 품사 태깅 된 결과에서 단어만 추출
words = [w for w, t in tagged_words]

# 불용어 (stop_word) 정의
ignored_words = [u'안녕'] # u는 유니코드

# finder 정의 : 콜로케이션 객체 생성
# finder = collocations.BigramCollocationFinder.from_words(words)
# finder = collocations.TrigramCollocationFinder.from_words(words)
finder = collocations.QuadgramCollocationFinder.from_words(words)

# 필터
# 단어 길이가 2 미만이거나, stopword에 포함될 경우 제외
finder.apply_word_filter(lambda w: len(w) < 2 or w in ignored_words)
# 빈도가 3 이하인 경우 제외
finder.apply_freq_filter(3)

# collocation 계산 후, 상위 10개 출력
pprint(finder.nbest(measures.pmi, 10))