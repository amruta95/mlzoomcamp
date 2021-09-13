import pandas as pd
import numpy as np

# Question 1
print("np version is :", np.__version__)

# Question 2
print("np version is :", pd.__version__)


# Question 3
!wget https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv

pd.set_option('display.max_columns', None)
df = pd.read_csv('data.csv')
print(df.head())
print(df)

df_BMW = df[
    df['Make'] == 'BMW'
]
print('The average price of the BMW is :', df_BMW['MSRP'].mean())


# Question 4
df_2015=df[df['Year'] >=2015
          ]
print(df_2015['Engine HP'].isnull().sum())


# Question 5
mean_hp_before = df['Engine HP'].mean()
print('Engine HP with NA values:', round(mean_hp_before,2))

df['Engine HP fillna'] = df['Engine HP'].fillna(df['Engine HP'].mean())
mean_hp_after = df['Engine HP fillna'].mean()
print('The Engine HP without NA values:', round(mean_hp_after,2))


# Question 6
x=np.array(df[df.Make == "Rolls Royce"][["Engine HP", "Engine Cylinders", "highway MPG"]].drop_duplicates())
print(x)
print(x.shape)

XTX =x.T.dot(x)
print(XTX)

XTX_invert=np.linalg.inv(XTX)
print(dfDirty, XTX_invert.sum())

# Question 7
y=np.array([1000,1100,900,1200,1000,850,1300])
w=(XTX_invert.dot(x,T)).dot(y)
print(w[0])