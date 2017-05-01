import pandas as pd
import random

data = pd.read_csv('movie_metadata.csv', index_col=False)

keep_col = ['director_name', 'num_critic_for_reviews', 'duration', 'director_facebook_likes',
            'actor_1_facebook_likes', 'gross', 'genres', 'actor_1_name', 'movie_title',
            'num_voted_users', 'cast_total_facebook_likes', 'num_user_for_reviews', 'language',
            'country', 'content_rating', 'budget', 'title_year', 'imdb_score', 'movie_facebook_likes']

new_file = data[keep_col]

new_data = new_file.fillna(new_file.mean())

new_data = new_data[new_data.language == 'English']
new_data = new_data[new_data.country == 'USA']

new_data = new_data[new_data.content_rating != 'TV-14']
new_data = new_data[new_data.content_rating != 'TV-PG']
new_data = new_data[new_data.content_rating != 'TV-MA']
new_data = new_data[new_data.content_rating != 'TV-G']
new_data = new_data[new_data.content_rating != 'TV-Y7']
new_data = new_data[new_data.content_rating != 'Passed']
new_data = new_data[new_data.content_rating != 'Approved']
new_data = new_data[new_data.content_rating != 'Not Rated']
new_data = new_data[new_data.content_rating != 'Unrated']
new_data = new_data[new_data.content_rating != 'NC-17']
new_data = new_data[pd.notnull(new_data['content_rating'])]

new_data = new_data.reset_index()

for i in range(0, len(new_data['genres'])):
    record = new_data.loc[i, 'genres']
    splitVal = record.split('|')
    val = random.choice(splitVal)
    new_data.iloc[i, new_data.columns.get_loc('genres')] = val

new_data = new_data.reset_index()

# for i in range(0, len(new_data['imdb_score'])):
#     rating = float(new_data.loc[i, 'imdb_score'])
#     if rating <= 10 and rating >= 7.5:
#         new_data.iloc[i, new_data.columns.get_loc('imdb_score')] = 4
#     if rating >= 5 and rating <= 7.4:
#         new_data.iloc[i, new_data.columns.get_loc('imdb_score')] = 3
#     if rating >= 2.5 and rating <= 4.9:
#         new_data.iloc[i, new_data.columns.get_loc('imdb_score')] = 2
#
#     if rating >= 1 and rating <= 2.4:
#         new_data.iloc[i, new_data.columns.get_loc('imdb_score')] = 1

# print(new_data['imdb_score'])
cleaned_data = new_data

cleaned_data.to_csv("cleaned_movie_metadata.csv",index =False)


