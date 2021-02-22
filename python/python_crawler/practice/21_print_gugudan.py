# 2단 출력
def print2Dan():
    for num in range (1, 9 + 1):
        result = 2 * num
        print('2 *',num,'=',result)
#print2Dan()

# 구구단 만들기 n
def printNDan(val1):
    for num in range (1, 9 + 1):
        result = val1 * num
        print(val1,'*',num,'=',result)

printNDan(3)