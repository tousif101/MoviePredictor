import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


"""
Open up the clean data
"""
data = pd.read_csv('cleaned_movie_metadata.csv', index_col=False)
del data['index']
del data['level_0']


"""
Now the data is clean for us to use and visualize the Data
"""

years = data["title_year"]
scores = data["imdb_score"]
ratings = data["content_rating"]
directors = data["director_name"]
actors = data["actor_1_name"]

durations = data["duration"]
directorFbLikes = data["director_facebook_likes"]
actorFbLikes = data["actor_1_facebook_likes"]
castTotalLikes = data["cast_total_facebook_likes"]
movieFbLikes = data["movie_facebook_likes"]
budgets = data["budget"]



averageYear = {}
for i in range(len(years)):
    year = years[i]
    rating = scores[i]
    if year in averageYear:
        averageYear[year].append(rating)
    else:
        averageYear[year] = [rating]


averageRecord = {}
for key in averageYear.keys():
    values = averageYear[key]
    total = sum(values)
    average = total/len(values)
    averageRecord[key] = average

averageYearToGraph = list(averageRecord.keys())
averageRatingToGraph = list(averageRecord.values())


yearCount = {}
for year in years:
    if year in yearCount:
        yearCount[year] = yearCount[year] + 1
    else:
        yearCount[year] = 1
yearCountYears = list(yearCount.keys())
yearCountNum = list(yearCount.values())

plt.figure(1)
plt.ylabel("Number Movies")
plt.xlabel("Year")
plt.title("Year vs Number")
plt.plot(yearCountYears, yearCountNum, "ro", markersize=3)

plt.plot(np.unique(yearCountYears), np.poly1d(np.polyfit(yearCountYears, yearCountNum, 2))(np.unique(yearCountYears)))
plt.show()


plt.figure(2)
plt.ylabel("Score")
plt.xlabel("Year")
plt.title("Year vs Score")
plt.plot(averageYearToGraph, averageRatingToGraph, "ro", markersize=3)

plt.plot(np.unique(averageYearToGraph), np.poly1d(np.polyfit(averageYearToGraph, averageRatingToGraph, 1))(np.unique(averageYearToGraph)))

plt.text(1985, 2, r'Line of Best Fit: f(x)=-0.0156x + 34.29', fontsize=13)
bestfit = np.poly1d(np.polyfit(averageYearToGraph, averageRatingToGraph, 1))
plt.show()



ratingsAndScore = {}
for i in range(len(ratings)):
    rate = ratings[i]
    score = scores[i]
    if rate in ratingsAndScore:
        ratingsAndScore[rate].append(score)
    else:
        ratingsAndScore[rate] = [score]

averageRatingScore = {}
for key in ratingsAndScore.keys():
    values = ratingsAndScore[key]
    total = sum(values)
    average = total/len(values)
    averageRatingScore[key] = average

plt.figure(3)
xRatings = list(averageRatingScore.keys())
yAverageRatingScore = list(averageRatingScore.values())

plt.bar(range(len(yAverageRatingScore)), yAverageRatingScore, align='center')
plt.xticks(range(len(yAverageRatingScore)), xRatings, size='small')
plt.ylabel("Average Score")
plt.xlabel("Ratings")
plt.title("Ratings vs Score")
plt.show()

directorScores = {}
for i in range(len(directors)):
    director = directors[i]
    score = scores[i]
    if director in directorScores:
        directorScores[director].append(score)
    else:
        directorScores[director] = [score]


averageDirectorScore = {}
for key in directorScores.keys():
    values = directorScores[key]
    total = sum(values)
    average = total/len(values)
    averageDirectorScore[key] = average

sortedDirector = sorted(averageDirectorScore, key=averageDirectorScore.get)
sortedDirectorScore = sorted(averageDirectorScore.values())


topTwentyDirectors = sortedDirector[-20:]
topTwentyAverages = sortedDirectorScore[-20:]

plt.figure(4)
plt.bar(range(len(topTwentyAverages)), topTwentyAverages, align='center')
plt.xticks(range(len(topTwentyDirectors)), topTwentyDirectors, size='small',rotation='vertical')
plt.ylabel("Average Score")
plt.xlabel("Directors")
plt.title("Director vs Score")
plt.show()

actorScores = {}
for i in range(len(actors)):
    actor = actors[i]
    score = scores[i]
    if actor in actorScores:
        actorScores[actor].append(score)
    else:
        actorScores[actor] = [score]

averageActorScore = {}
for key in actorScores.keys():
    values = actorScores[key]
    total = sum(values)
    average = total/len(values)
    averageActorScore[key] = average

sortedActor = sorted(averageActorScore, key=averageActorScore.get)
sortedActorScore = sorted(averageActorScore.values())


topTwentyActor = sortedActor[-20:]
topTwentyActorAverages = sortedActorScore[-20:]

plt.figure(5)
plt.bar(range(len(topTwentyActorAverages)), topTwentyActorAverages, align='center')
plt.xticks(range(len(topTwentyActor)), topTwentyActor, size='small',rotation='vertical')
plt.ylabel("Average Score")
plt.xlabel("Actors")
plt.title("Actors vs Score")
plt.show()

plt.figure(6)
plt.ylabel("IMDB Score")
plt.xlabel("Movie Facebook Like")
plt.title("Movie Likes vs IMDB Score")
plt.plot(movieFbLikes, scores, "ro", markersize=3)
plt.show()

plt.figure(7)
plt.ylabel("Budget")
plt.xlabel("Cast Facebook Like")
plt.title("Cast Likes vs Budget")
plt.plot(castTotalLikes, budgets, "ro", markersize=3)
plt.show()

plt.figure(8)
plt.ylabel("IMDB Score")
plt.xlabel("Director Likes")
plt.title("Director Likes vs Score")
plt.plot(directorFbLikes, scores, "ro", markersize=3)
plt.show()

plt.figure(9)
plt.ylabel("IMDB Score")
plt.xlabel("Actor Likes")
plt.title("Actor Likes vs Score")
plt.plot(actorFbLikes, scores, "ro", markersize=3)
plt.show()

plt.figure(10)
plt.ylabel("IMDB Score")
plt.xlabel("Duration")
plt.title("Duration vs Score")
plt.plot(durations, scores, "ro", markersize=3)
plt.show()











