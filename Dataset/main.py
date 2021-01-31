import random

import pandas as pd

# setting the 3rd row as header. 
df = pd.read_csv("C:\\Users\\MADHUR\\PycharmProjects\\Question\\urls.csv")
df2= pd.DataFrame()
i=0
for x in range(0,2500):
    i = random.randint(0, 10000)
    df2 = df2.append(df.iloc[i])

df2.to_csv('file_name.csv')
frames = [df,df2]
df = pd.concat(frames)

df.to_csv('updated_urls3.csv')

