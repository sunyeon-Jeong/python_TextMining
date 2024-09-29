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