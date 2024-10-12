'''
1. Bag of Words(BoW)
- 각 단어에 고유한 정수 인덱스 부여 -> 벡터 생성 -> 각 단어 등장횟수 기록
- 문서에 포함된 단어의 빈도를 벡터 형태로 표출 (build_bag_of_words 함수)
'''
from nltk.tokenize import TreebankWordTokenizer

def build_bag_of_words(doc):
    
    # 온점 제거 및 토큰화 진행
    doc = doc.replace('.', '')
    tokenized_document = TreebankWordTokenizer().tokenize(doc)
    
    # 단어 <-> 인덱스 매핑 딕셔너리
    word_to_index = {}
    
    # BoW를 저장할 리스트 (단어 빈도)
    bow = []
    
    for word in tokenized_document:
        
        # 단어가 처음 등장 -> 인덱스 부여, BoW에 1 추가
        if word not in word_to_index.keys():
            word_to_index[word] = len(word_to_index)
            bow.insert(len(word_to_index) -1, 1)
        
        # 이미 등장한 단어 -> 해당 인덱스 위치의 BoW 값에 1 추가
        else:
            index = word_to_index.get(word)
            bow[index] = bow[index] + 1
    
    return word_to_index, bow

doc1 = "Imagination is more important than knowledge"

vocab, bow = build_bag_of_words(doc1)

print('vocabulary : ', vocab)
print('bag of words vector : ', bow)

doc2 = "Knowledge is limited"

vocab, bow = build_bag_of_words(doc2)

print('vocabulary : ', vocab)
print('bag of words vector : ', bow)

doc3 = "Imagenation encircles the world"

vocab, bow = build_bag_of_words(doc3)

print('vocabulary : ', vocab)
print('bag of words vector : ', bow)

doc4 = doc1 + " " + doc2 + " " + doc3

vocab, bow = build_bag_of_words(doc4)

print('vocabulary : ', vocab)
print('bag of words vector : ', bow)