import pandas as pd
df = pd.read_csv("C:\\Users\\Analinear-PC49\\students.csv")
print(df.dropna())
print(df.fillna("Unknown"))