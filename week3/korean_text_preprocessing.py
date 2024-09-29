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

