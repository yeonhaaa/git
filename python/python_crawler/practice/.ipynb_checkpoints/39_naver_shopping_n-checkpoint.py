import requests
from bs4 import BeautifulSoup
# 특정 정보만 불러오고 싶을 때는 from 사용한다.(BeautifulSoup이라는 함수 하나만 불러오고 싶음)

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ulTag = bsObj.find("ul", {"class":"list_basis"})
    lis = ulTag.findAll("li", {"class":"basicList_item__2XT81 ad"})     # 광고 쇼핑몰
    # lis = ulTag.findAll("li", {"class":"basicList_item__2XT81"})
    # findAll 쓰면 list [] 형식으로 반환해준다.

    # li = lis[0]                 # 첫번째 상품 정보 가져오기
    # print(len(lis))
    # print(li)
    # basicList =  li.find("div", {"class":"basicList_title__3P9Q7"})
    # aTags = basicList('a', {"class":"basicList_link__1MaTN"})
    # aTag = aTags[0]             # aTags 출력하면 []형식으로 나옴. <>형식으로 바꾸준다.
    # link = aTag['href']
    # title = aTag['title']
    # priceNum = li.find("span", {"class":"price_num__2WUXn"})
    # price = priceNum.text
    # # print(price) 잘 나오는지 확인!
    # print(title, price, link)

    # 첫번째, 두번째, ...상품 한번에 가져오기 -> 반복문 사용
    for li in lis[:3]:
        try:
            info = li.find("div", {"class": "basicList_info_area__17Xyo"})
            aTag = info.find('a')
            title = aTag['title']
            link = aTag['href']

            priceNum = li.find("span", {"class": "price_num__2WUXn"})
            price = priceNum.text
            print(title, price, link)
        except Exception as e:
            print("-----error-----", e)

    return [{},{},{},{}]        # 한 페이지에 여러 정보가 나오므로 리스트 형식[] 사용.

# 셔츠 검색
url = "https://search.shopping.naver.com/search/all?query=%EC%85%94%EC%B8%A0&frm=NVSHATC&prevQuery=%EC%85%94%EC%B8%A0"
pageString = crawl(url)
#print(pageString)
products = parse(pageString)
print(products)