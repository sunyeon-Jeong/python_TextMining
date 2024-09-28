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
1-1. 단어 토큰화 : nltk (word/WordPunct/TreebankWord_tokenize)
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

'''
1-2. 문장 토큰화 : nltk (sent_tokenize)
'''
from nltk.tokenize import sent_tokenize

text = """Cosmos is a Greek word for the order of the universe.
It is, in a way, the opposite of Chaos.
It implies the deep interconnectedness of all things.
It conveys awe for the intricate and subtle way in which the universe is put together."""

# 문장 단위로 텍스트 분할
print(sent_tokenize(text))

text = "I am actively looking for Ph.D. students. and you are a Ph.D student."

# 문장 단위로 텍스트 분할
print(sent_tokenize(text))
