# getSalary() 연봉 구하기 연차 * 2000만원
# getVAT() 부가가치세 money * 0.1
# 내 연봉에 대한 부가가치세가 얼마일까?

def getSalary(year):
    return year * 20_000_000
def getVAT(money):
    return money * 0.1

# g o f -> getVAT o getSalary(3)
mySalary = getSalary(3)
myVat = getVAT(mySalary)
print(myVat)

print(getVAT(getSalary(3)))