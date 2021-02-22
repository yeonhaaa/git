# 합성함수 연산 시 반드시 return을 써야함!! (안쓰면 None이 나옴)
def f(x):
    return x + 1
def g(x):
    return x / 2

# g o f(x) -> parse_o_crawl(x)
# g o f(10) = ?

resF = f(10) #11
resG = g(resF) #5.5
print(resG)

result = g(f(10))
print(result)