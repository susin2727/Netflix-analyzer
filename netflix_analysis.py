import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

#============LOADING THE DATASET=============

df = pd.read_csv("netflix_titles.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())

#===========MISSING VALUES=============== 
df['director'].fillna("Unknown", inplace=True)
df['country'].fillna("Unknown", inplace=True)
df['cast'].fillna("Not Available", inplace=True)
df['rating'].fillna(df['rating'].mode()[0], inplace=True)
df['date_added'].fillna("Unknown", inplace=True)

#==========DUPLICATE RECORDS===============
print("Duplicates:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

#============CONVERT DATE==================
df['date_added'] = pd.to_datetime(
    df['date_added'],
    errors='coerce'
)
df['year_added'] = df['date_added'].dt.year



#============VISUALIZATION 1================
plt.figure(figsize=(6,4))
sns.countplot(
    x='type',
    data=df
)
plt.title("Movies vs TV Shows")
plt.show()

#=============VISUALIZATION 2=================
top_country = df['country'].value_counts().head(10)
plt.figure(figsize=(10,5))
top_country.plot(kind='bar')
plt.title("Top 10 Countries Producing Netflix Content")
plt.show()

#==============VISUALIZATION 3================
plt.figure(figsize=(10,5))
sns.countplot(
    y='rating',
    data=df,
    order=df['rating'].value_counts().index
)
plt.title("Content Rating Distribution")
plt.show()

#===============VISUALIZATION 4================
year_data = df['year_added'].value_counts().sort_index()
plt.figure(figsize=(12,5))
year_data.plot()
plt.title("Content Added Over Years")
plt.show()

#=================VISUALIZATION 5===============
top_genres = df['listed_in'].str.split(', ').explode()
top_genres.value_counts().head(10).plot(
    kind='barh'
)
plt.title("Top Genres")
plt.show()

