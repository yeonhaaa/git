import pandas as pd
pd.set_option('display.max_colwidth',-1)

df = pd.read_json("./shirts.json")
# print(df.count())
# print(df.head(10))

# 특정 브랜드 필터링 ( 노출 수 검색 )
def printBrandCount(keyword):
    dfFiltered = df[df['title'].str.contains(keyword)]
    print(dfFiltered.count())

brands = ['킨더살몬', '지오다노', '유라고']
for brand in brands:
    printBrandCount(brand)

# 가격 필터링
print(type(df['price']) )
def printPriceRange(price1, price2):
    dfFiltered = df[(df['price'] <= price1) & (df['price'] <= price1)]
    dfSorted = dfFiltered.sort_values(['price'],ascending=[0])
    print(dfSorted.head(10)['price'])
    print(dfSorted.tail(10)['price'])
    print(dfFiltered['price'] .count())

printPriceRange(10000,20000)