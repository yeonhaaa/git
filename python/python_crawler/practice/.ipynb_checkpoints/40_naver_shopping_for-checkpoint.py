import requests
from bs4 import BeautifulSoup
# 특정 정보만 불러오고 싶을 때는 from 사용한다.(BeautifulSoup이라는 함수 하나만 불러오고 싶음)

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def getProductInfo(li):
    info = li.find("div", {"class": "basicList_info_area__17Xyo"})
    aTag = info.find('a')
    title = aTag['title']
    link = aTag['href']
    priceNum = li.find("span", {"class": "price_num__2WUXn"})
    price = priceNum.text
    price = price.replace(",","").replace(","," ")       # 10,000 -> 10000 변경
    #print(title, price, link)
    return {"title":title, "price":price, "link":link}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ulTag = bsObj.find("ul", {"class":"list_basis"})
    # lis_ad = ulTag.findAll("li", {"class":"basicList_item__2XT81 ad"})
    lis = ulTag.findAll("li", {"class":"basicList_item__2XT81"})    # findAll 쓰면 list [] 형식으로 반환해준다.

    # 반복문 사용 -> 첫번째, 두번째, ...상품 한번에 가져오기
    products = []
    for li in lis[:5]:
        try:
            productInfo = getProductInfo(li)
            products.append(productInfo)
        except Exception as e:
            print("-----error-----",e)

    return products

# 가디건 검색

def getPageResult(pageNo,keyword):
    url = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EA%B0%80%EB%94%94%EA%B1%B4&pagingIndex={}&pagingSize=40&productSet=total&query={}&sort=rel&timestamp=&viewType=list".format(pageNo,keyword)
    pageString = crawl(url)
    products = parse(pageString)
    return products

pageResultTotal = []
for pageNo in (1,10+1):
    pageResultTotal = pageResultTotal + getPageResult(pageNo,"셔츠")
print(len(pageResultTotal))

import json
file = open("./shirts.json","w+")
file.write(json.dumps(pageResultTotal))