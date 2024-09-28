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

'''
2. 표제어 추출 (Lemmatization) : nltk (WordNetLemmatizer)
'''
from nltk.stem import WordNetLemmatizer

# 객체 생성
lemmatizer = WordNetLemmatizer()

words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']

print('표제어 추출 전 : ', words)

# 각 단어의 표제어 추출 : 기본 사전형 단어로 변형 (어근)
print('표제어 추출 후 : ', [lemmatizer.lemmatize(word) for word in words])

# 각 단어의 동사 품사로 표제어 추출
print('dies의 동사 표제어 : ', lemmatizer.lemmatize('dies', 'v'))
print('watched의 동사 표제어 : ', lemmatizer.lemmatize('watched', 'v'))
print('has의 동사 표제어 : ', lemmatizer.lemmatize('has', 'v'))