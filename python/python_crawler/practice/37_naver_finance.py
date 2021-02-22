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
    #print(price)
    return {"price:",price}

url = "https://finance.naver.com/item/main.nhn?code=000660"
pageString = crawl(url)
companyInfo = parse(pageString)
print(companyInfo)
