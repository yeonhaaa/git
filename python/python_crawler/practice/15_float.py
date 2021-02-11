# 소수점 float
val1 = 0.1
val2 = 0.2
print(type(val1), type(val2)) # float
print(type(1), type(2)) # 정수 integer

def devide(val1, val2):
    print("=>", type(val1), type(val2))
    result = val1 / val2
    print(result, type(result))

devide(10, 20) #0.5
