# crawl, parse
import requests
from bs4 import BeautifulSoup
def crawl(url):
    data = requests.get(url)
   # print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    noToday = bsObj.find("p" ,{"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})
    price = blind.text
    #print(blind)
    wrapCompany = bsObj.find("div", {"class":"wrap_company"})
    aTag = wrapCompany.find("a")
    name = aTag.text
    #print(aTag)
    description = bsObj.find("div", {"class":"description"})
    spanTag = description.find("span", {"class":"code"})
    code = spanTag.text
    img = description.find("img")
    category = img['alt'] # img 태그 안의 속성 alt 접근
    catEng = img['class'] # img 태그 안의 속성 class 접근
    #print(img)
    return {"name":name, "price":price, "code":code
            , "category":category, "catEng":catEng[0]}
# 삼성전자 : 005930 / 카카오 : 035720 / SK하이닉스 :
def getCompanyInfo(code):
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    pageString = crawl(url)
    companyInfo = parse(pageString)
    return companyInfo

codes = ["005930", "035720", "000660"]
for code in codes :
    print(getCompanyInfo(code))
