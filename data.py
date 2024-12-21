import pandas as pd

df = pd.read_csv("C:/Users/Admin/health-lifestyle/Sleep_health_and_lifestyle_dataset.csv")

df

df.shape

df.info

df.head(10)
df.tail(10)
df.head(10)

df.drop_duplicates()

df.fillna(0)

import matplotlib.pyplot as plt

df.columns

df[['Gender', 'Stress Level']].plot(kind='line') 
