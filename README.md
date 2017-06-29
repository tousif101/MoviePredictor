# MoviePredictor
Uses Pandas for Data Cleaning and use Scikit-Learn machine learning algorithm to create a movie rating system. 

## Running 
Please run movie_data_clean.py in the same directory as the original csv file. The run the data_visualization.py file to get a visual representation of cool trends and the performances of the machine learning algorithms. Finally run movie_classification.py to classify the data. 

## Goals
The goal of the project was to try to predict how good a movie will be, before it is released. Initial data source is from Kaggle dataset. https://www.kaggle.com/deepmatrix/imdb-5000-movie-dataset.

## Data Cleaning
Data cleaning was by far the longest the hardest and part. I kept only the columns I needed like 'director_name', 'num_critic_for_reviews', 'duration', 'director_facebook_likes','actor_1_facebook_likes', 'gross', 'genres', 'actor_1_name', 'movie_title', 'num_voted_users', 'cast_total_facebook_likes', 'num_user_for_reviews', 'language', 'country', 'content_rating', 'budget', 'title_year', 'imdb_score', 'movie_facebook_likes'. I then filtered for only country and language to get all American English movies. There was a lot more I could have done for this section, and my future plans are to learn better data preprocessing techniques and get better data. 

## Results
After running a few algorithms, the ANN had an 80% accuracy rate. 

## What I Learned and Plans 
I learned that predicting movie data is insanely hard because there are alot of different attributes. What I could have done better, definetly the data cleaning and preprocessing part. Future plans are to improve the data pre-processing, getting my own data using web scrappers and other APIs and databases and improve my machine learning algorithms. 
