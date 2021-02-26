# list를 반복문 사용해서 꺼내기
# list는 가독성을 위해 세로로 쓰기도 한다.
names = [
    'haha',
    'hoho',
    'hihi',
    'huhu'
]

for name in names:
    print(name)

def printMessage(name):
    message = "{}님 안녕!".format(name)
    print(message)

printMessage(names[0])
printMessage(names[1])
printMessage(names[2])
print('---')

# 반복문 사용해서 한번에 호출
for name in names:
    printMessage(name)

# list 반복문
numbers = [1,2,3,4,5]
for num in numbers :
    print(num)

products = [{},{},{}]
for product in products :
    print(product)