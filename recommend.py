import numpy as np
import pandas as pd

ratings_data = pd.read_csv('C:\Users\Shoto\PycharmProjects\Movie_Recommender\ml-latest-small\\ratings.csv')
# print ratings_data.head()

movies_info = pd.read_csv('C:\Users\Shoto\PycharmProjects\Movie_Recommender\ml-latest-small\movies.csv')
# print movies_info.head()

movie_data = pd.merge(ratings_data, movies_info, on='movieId')
# print movie_data.head()

movie_data.groupby('title')['rating'].mean().sort_values(ascending=False)
# print movie_data.head()

# print movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head()

ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())
print ratings_mean_count.head()
