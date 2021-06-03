# 크롤링 파싱 스크래핑
# crawl() -> 데이터 받아오기
# parse() -> 받아온 데이터에서 필요한 정보 뽑
# g o f(x) -> parse o crawl(url) : url받아와서 파싱하는 합성함수형태
# crawl -> requests
# parse -> bs4
# <Response [200]> -> 호출 성공

import requests
def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

# crawl(url) -> data 받아오는 함수
url = "https://finance.naver.com/item/main.nhn?code=035720"
pageString = crawl(url)
print(pageString)