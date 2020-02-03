import pandas as pd
import csv

df = pd.read_csv("sentiment.csv")
df = df.mean()
df = df.drop(["neu", "compound"])

print("\n----------- Calculate Mean -----------\n")
print(df)