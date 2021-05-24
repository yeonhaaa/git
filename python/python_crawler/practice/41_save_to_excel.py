import pandas as pd

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer,'Sheet1')
    writer.save()

# datafram -> 표
df = pd.read_json("./shirts.json")
print(df.count())

save(df, "./shirts.xlsx")