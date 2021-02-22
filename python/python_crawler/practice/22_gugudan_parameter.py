# n단 format 사용
def printNdan(dan):
    for num in range (1, 9 + 1):
        gugudan = "{} * {} = {}".format(dan, num, dan * num)
        print(gugudan)
    print('------')
printNdan(14)
printNdan(4)

# 100단 까지 호출 반복
for dan in range (2,100 + 1):
    printNdan(dan)