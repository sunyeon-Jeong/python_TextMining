'''
Author : 202210587 미래학부 정선연
createdAt : 240929
'''

'''
0. NLTK 라이브러리 다운로드
'''
import nltk

# 토크나이저 모듈
nltk.download('punkt')

# 표제어추출 모듈
nltk.download('wordnet')

# 불용어 제거 모듈
nltk.download('stopwords')

# 품사 태깅 모듈
nltk.download('averaged_perceptron_tagger')

'''
1. 토큰화 (Tokenization)
'''
from nltk.tokenize import TreebankWordTokenizer

text = "I'm back-end developer, mallang. I majored in BigData & AI"

# TreebankWordTokenizer 사용
print('TreebankWordTokenizer : ', TreebankWordTokenizer().tokenize(text))

'''
2. 표제어추출 (Lemmatization)
'''
from nltk.stem import WordNetLemmatizer

# 객체생성
lemmatizer = WordNetLemmatizer()

words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives',
         'fly', 'dies', 'watched', 'has', 'starting']

print('표제어 추출 전 : ', words)
print('표제어 추출 후 : ', [lemmatizer.lemmatize(word) for word in words])

# 각 단어의 동사 품사로 표제어 추출
print('dies의 동사 표제어 : ', lemmatizer.lemmatize('dies', 'v'))
print('watched의 동사 표제어 : ', lemmatizer.lemmatize('watched', 'v'))
print('has의 동사 표제어 : ', lemmatizer.lemmatize('has', 'v'))

'''
3. 불용어 제거와 품사 태깅
'''
# 불용어 모듈
from nltk.corpus import stopwords
# 토크나이저 모듈
from nltk.tokenize import word_tokenize

# 영어 불용어 리스트
stop_words_list = stopwords.words('english')

print('불용어 개수 : ', len(stop_words_list))
print('불용어 출력 : ', stop_words_list)

text = "The grass is always greener on the other side of the fence."

# 영어 불용어 집합
stop_words = set(stopwords.words('english'))

# 영어 텍스트 토큰화
word_tokens = word_tokenize(text)

result = []
for word in word_tokens:
    if word not in stop_words:
        result.append(word)
        
print('불용어 제거 전 : ', word_tokens)
print('불용어 제거 후 : ', result)

# 토큰 품사 태깅
print(nltk.pos_tag(result))