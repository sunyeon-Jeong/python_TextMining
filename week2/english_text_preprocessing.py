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
nltk.download('averaged_perceptron_tagger_eng')

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
- 
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

'''
3. 어간추출 (Stemming) : nltk.stem
- 정해진 규칙만 보고 단어의 어미를 어림짐작하여 자름
'''
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

porter_Stemmer = PorterStemmer()
lancaster_Stemmer = LancasterStemmer()

words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives',
         'fly', 'dies', 'watched', 'has', 'starting']

print('어간 추출 전 : ', words)

# 포터스테머로 어간 추출
print('PorterStemmer 어간 추출 후 : ', [porter_Stemmer.stem(word) for word in words])

# 랭커스터스테머로 어간 추출
print('LancasterStemmer 어간 추출 후 : ', [lancaster_Stemmer.stem(word) for word in words])

'''
4. 정규표현식 (Regular Expression) : nltk.tokenize (RegexpTokenizer)
- 검색하는 모듈
- 다른 토크나이저에 비해 융통성이 있는 편 (표현방식 지정이 가능하기 때문에)
'''
import re

# []에 해당하는 문자 출력
print(re.findall('[abc]', 'How are you, boy?'))

# []에 해당하는 문자 출력
print(re.findall('[0123456789]', '3a5b7c9d'))

# 토크나이저 조건을 직접 지정
from nltk.tokenize import RegexpTokenizer

text = 'Mr. Jone’s Orphanage is as cheery as cheery goes for a pastry shop'

# 문자, 숫자, '를 포함해 단어 구분
tokenizer = RegexpTokenizer('[\w]+')
print(tokenizer.tokenize(text))

# '를 포함해 3글자 이상 단어 구분
tokenizer = RegexpTokenizer("[\w']{3,}")
print(tokenizer.tokenize(text))

'''
5. 불용어 제거와 품사태깅
'''
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words_list = stopwords.words('english')

# 라이브러리에서 정의하고 있는 불용어 판단 기준 수정(커스텀)가능
print('불용어 개수 : ', len(stop_words_list))
print('불용어 출력 : ', stop_words_list)

text = "Family is not an important thing. It's everything."

stop_words = set(stopwords.words('english')) # 영어 불용어 집합

word_tokens = word_tokenize(text)

result = []
for word in word_tokens:
    if word not in stop_words:
        result.append(word)
        
print('불용어 제거 전 : ', word_tokens)
print('불용어 제거 후 : ', result)

# 토큰 품사 태깅
print(nltk.pos_tag(result))