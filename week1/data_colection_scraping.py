'''
0. 라이브러리 불러오기
'''
# 웹페이지에 데이터 요청 & HTML, XML 등의 문서 파싱, 데이터 추출
import urllib.request as request
from bs4 import BeautifulSoup

'''
1. BeautifulSoup을 이용한 스크래핑(로컬파일)
- with open() -> 로컬 HTML 파일을 읽음
- BeautifulSoup을 이용해 HTML 파일 파싱 & 정보 추출
'''
# 파일 읽기 -> 파일내용 저장
with open('/Users/sunyeonjeong/dev/github/textMining/week1/tda.html', 'r') as f:
    html_doc = f.read()

print(html_doc)

# html.parser 파싱
soup = BeautifulSoup(html_doc, 'html.parser')

# 포매팅 된 형태로 파싱된 웹페이지 소스코드 출력
print(soup.prettify())

# <p>태그 찾아서 반환
soup.find('p')

# <p>태그 문자열 반환
soup.find('p').string

# herf 속성이 홈페이진 요소를 찾아서 반환
soup.find(attrs={'herf' : 'https://www.cuk.edu/'})

# 모든 <p>태그 요소 -> 리스트로 반환
soup.find_all('p')

'''
2. BeautifulSoup을 이용한 인터넷 웹페이지 스크래핑
- FnGuide 웹페이지 접속
- 웹페이지 소스 -> BeautifulSoup으로 파싱 -> 필요정보 추출
'''

# 크롤링 대상 url
url = 'https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN='

# url을 통해 웹페이지 접속
res = request.urlopen(url)

# 웹페이지 소스코드 -> html.parser로 파싱
soup = BeautifulSoup(res, "html.parser")

# id속성이 bizSummaryDate인 요소를 찾아 변수에 저장
bizSummaryDate = soup.find(attrs={'id' : 'bizSummeryDate'})

# id속성이 bizSummaryHeader인 요소를 찾아 변수에 저장
bizSummaryHeader = soup.find(attrs={'id' : 'bizSummeryHeader'})
