import requests
from bs4 import BeautifulSoup

# crawl -> data 받아오기
# parse -> 정보 뽑아내기 price

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    noToday = bsObj.find("p", {"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})
    price = blind.text
    #print(blind)
    #print(noToday)
    #print(bsObj)
    return price

    # 서울시 강남구 서초동 899-1122
    # tag, class div, a, p, span -> 태그 <div>내용</div>
    # class <p class="no_today"> 내용 </p>
    # bsObj = 대한민국, tag = 서울시 강남구 , class = 서초동 899-1122

# g o f(x) -> parse o crawl(url)
#url = "https://finance.naver.com/item/main.nhn?code=035720" #카카오
url = "https://finance.naver.com/item/main.nhn?code=005930" #삼전
pageString = crawl(url)
price = parse(pageString)
print("price :", price)