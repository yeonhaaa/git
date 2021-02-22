# 연봉 = 연차(year) * 900 만원
def getSalary(year):
    return year * 9_000_000

years = [2, 8, 4, 5] # -> [18, 72, 36, 45]

def getResult(years):
    salaryList = []
    for year in years:
        salary = getSalary(year)
        salaryList.append(salary)
    print(salaryList)

getResult(years)
result = getResult(years)
print('result:', result)