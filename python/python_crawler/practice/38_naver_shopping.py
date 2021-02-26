import requests
from bs4 import BeautifulSoup
# 특정 정보만 불러오고 싶을 때는 from 사용한다.(BeautifulSoup이라는 함수 하나만 불러오고 싶음)

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    info = bsObj.find('div', {'class':'basicList_title__3P9Q7'})
    aTag = info.find('a')
    title = aTag['title'] # 상품 이름
    link = aTag['href'] # 상품 링크

    priceNum = bsObj.find('span', {'class':'price_num__2WUXn'})
    price = priceNum.text # 상품 가격

    productInfo = {"title":title, "price":price, "link":link}
    print(productInfo)
    #print(title, price, link)
    #name = aTag.text
    return [{},{},{},{}] # 한 페이지에 여러 정보가 나오므로 리스트 형식[] 사용.

url = "https://search.shopping.naver.com/search/all?query=%EC%85%94%EC%B8%A0&cat_id=&frm=NVSHATC"
pageString = crawl(url)
#print(pageString)
products = parse(pageString)
print(products)