import pandas as pd 
#Нужно узнать зависит ли баллы по атематике от образования родителей
df = pd.read_csv("StudentsPerformance.csv")
df.info()
#print(df["math score"].mean())
print(df["parental level of education"].value_counts())
print(df.groupby(by=df["parental level of education"])["math score"].mean())