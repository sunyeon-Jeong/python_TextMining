'''
0. 라이브러리 불러오기
'''
import urllib.parse
import urllib.request
import json
import requests
import pandas as pd

'''
1. 네이버 검색 API 활용 -> 블로그 텍스트 수집
- 네이버 검색 API를 사용하여 키워드로 검색한 결과를 JSON 형식으로 변환
- pandas 라이브러리 사용을 통해 JSON을 pandas dataframe으로 변환하고 CSV 파일로 저장
'''
# 네이버 API 요청을 위한 Client 정보
client_id = "70SMDCFSUuauHFktee4q"
client_secret = "6myOUqZV7Y"

# 검색 쿼리 문자열 -> 아스키코드로 변환
# urllib.parse.quote() : url 인코딩
encText = urllib.parse.quote("부산 맛집")
print(encText) # %EB%B6%80%EC%82%B0%20%EB%A7%9B%EC%A7%91

# 페이징 (Naver API Docs 파라미터 정책 참고)
display = '&display=15' # 한 페이지에 표시할 검색결과 개수
sort = '&sort=date' # 정렬 옵션

# 네이버블로그 검색 API URL
url = "https://openapi.naver.com/v1/search/blog?query=" + encText + display + sort

# 네이버 API 요청을 위한 헤더설정
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

# 네이버 API 서버에 Reqeust 후, Response 받기
response = urllib.request.urlopen(request)

# 응답 상태 코드 확인
rescode = response.getcode()
print(rescode)

if rescode == 200:
    response_body = response.read()
    
    # Response -> JSON으로 변환 dictionary로 저장
    result = json.loads(response_body)
    
    # 결과 기반 DataFrame 생성
    df = pd.DataFrame(result['items'])
    
    # DataFrame CSV파일로 지정, 한글깨짐 방지를 위해 인코딩 utf-8-sig로 지정
    df.to_csv("/Users/sunyeonjeong/dev/github/textMining/week1/dataset/naverBlog_data.csv", index=False, encoding="utf-8-sig")
else:
    print("Error Code : " + rescode)
    
'''
2. 텍스트 데이터 수집결과 확인
'''
type(response_body)

print(response_body.decode('utf-8'))

type(result)

result

type(df)

df