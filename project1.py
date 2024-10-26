# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 00:41:58 2024

@author: User
"""
# CSS-D Project - Option 1: IMDB Data:

# Loading the Data:
import pandas as pd

df = pd.read_csv("movie_dataset.csv")

# Data Cleaning:
    
# Removing the "Index" column:
df = pd.read_csv("movie_dataset.csv",index_col=0)

# Dealing with the missing values in the "Revenue (Millions)" column by replacing them with the mean of the column:
avg_revenue = df["Revenue (Millions)"].mean()
df["Revenue (Millions)"].fillna(avg_revenue, inplace = True) 
    
"""
# Dealing with the missing values in the "Metascore" column by replacing them with the mean of the column and changing
the filled in values into integer to match the variable type of every other value in the column:
"""
avg_meta = df["Metascore"].mean()
df["Metascore"].fillna(avg_meta, inplace = True) 
df['Metascore'] = df['Metascore'].astype(int)

# Removing any duplicate rows if there is any:
df.drop_duplicates(inplace = True)

# Answering the Quiz questions:
    
# 1- What is the highest rated movie in the dataset?
max_rating = df["Rating"].max()
print("\nThe highest rated movie in the dataset is:\n",df[df["Rating"] == df["Rating"].max()]["Title"])

# 2- What is the average revenue of all movies in the dataset?
avg_revenue = df["Revenue (Millions)"].mean()
print("\nThe average revenue of all movies in the dataset is:\n",avg_revenue) 

# 3- What is the average revenue of movies from 2015 to 2017 in the dataset?
a = df[df['Year'] >= 2015]
a = a[a['Year'] <= 2017]
avg_revenue_2015_to_2017 = a["Revenue (Millions)"].mean()
print("\nThe average revenue of movies from 2015 to 2017 in the dataset is:\n", avg_revenue_2015_to_2017)

# 4- How many movies were released in the year 2016?
b = df[df['Year'] == 2016]
movies_released_2016 = b.count()
print("\nThe amount of movies released in the year 2016 is:\n", movies_released_2016)

# 5- How many movies were directed by Christopher Nolan?
c = df[df['Director'] == 'Christopher Nolan']
C_Nolan_movies = c.count()
print("\nThe amount of movies directed by Christopher Nolan is:\n", C_Nolan_movies)

# 6- How many movies in the dataset have a rating of at least 8.0?
d = df[df['Rating'] >= 8.0]
movies_rating_8_or_higher = d.count()
print("\nThe amount of movies in the dataset with a rating of at least 8.0 is:\n", movies_rating_8_or_higher)

# 7- What is the median rating of movies directed by Christopher Nolan?
median_rating_C_Nolan_movies = c["Rating"].median()
print("\nThe median rating of movies directed by Christopher Nolan is:\n", median_rating_C_Nolan_movies)

# 8- Find the year with the highest average rating
year_with_highest_average_rating = df.groupby('Year')['Rating'].mean().idxmax()
print("\nThe year with the highest average rating is:\n", year_with_highest_average_rating)

# 9- What is the percentage increase in number of movies made between 2006 and 2016?
e = df[df['Year'] == 2006]
movies_released_2006 = e.count()
percentage_increase_movie_number_between_2006_and_2016 = ((movies_released_2016 - movies_released_2006)/movies_released_2006)*100
print("\nThe percentage increase in number of movies made between 2006 and 2016 is:\n", percentage_increase_movie_number_between_2006_and_2016)

# 10- Find the most common actor in all the movies
most_common_actor_in_all_movies = df['Actors'].str.split(', ').explode().value_counts().idxmax()
print("\nThe most common actor in all the movies is:\n", most_common_actor_in_all_movies)

# 11- How many unique genres are there in the dataset?
unique_genres = df['Genre'].str.split(',').explode().value_counts().count()
print("\nThe amount of unique genres in the dataset is:\n", unique_genres)





 


























