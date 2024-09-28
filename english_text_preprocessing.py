'''
0. 라이브러리 불러오기
'''
# NLTK 라이브러리 : Natural Language Toolkit (자연어 처리 도구 모음)
import nltk
nltk.download()

# 토크나이저 모듈
nltk.download('punkt')
nltk.download('punkt_tab')
# 표제어 추출 모듈
nltk.download('wordnet')
# 불용어 제거 모듈
nltk.download('stopwords')
# 품사 태깅 모듈
nltk.download('averaged_perceptron_tagger')

'''
1. 토큰화
'''
'''
1-1. 단어 토큰화
- 텍스트 데이터의 특성과 사용 목적에 따라 토큰화 방법 선택
- word_tokenize, WordPunctTokenizer, TreebankWordTokenizer 모듈
'''
from nltk.tokenize import word_tokenize, WordPunctTokenizer, TreebankWordTokenizer

text = "You can't judge a book by its cover."

# word_tokenize 사용
print('word_tokenize : ', word_tokenize(text))

# WordPunctTokenizer 사용
print('WordPunctTokenizer: ', WordPunctTokenizer().tokenize(text))

# TreebankWordTokenizer 사용 (Penn Treebank Tokenization)
print('TreebankWordTokenizer: ', TreebankWordTokenizer().tokenize(text))
