val1 = 1 # 숫자형
print(val1)
val2 = "1" # 문자
print(val2)

print(val1 + 20) # 21
#print(val2 + 20) # 에러
print(type(val2))
print(int(val2) + 20) # 21

# 숫자형 -> 문자열
result = val2 + str(20) # 120
print(result, type(result))
print(int(result) + int("40"))
print(int(result) + 40)