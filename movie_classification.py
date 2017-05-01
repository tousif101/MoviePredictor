import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier

"""
Use these imports in the future to draw the ROC curves
for each predictive model.
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from scipy import interp
from sklearn.metrics import roc_curve, auc
"""
Even More Data Cleaning
Convert the genre, rating and imdb_score

SKIP AHEAD IF YOU ALREADY HAVE THE CLEAN DATA, OR ELSE RUN THIS
AND MARK DOWN THE NUMBER CONVERSIONS OF THE GENRE AND RATINGS
"""

# data = pd.read_csv('cleaned_movie_metadata.csv', index_col=False)
# del data['index']
# del data['level_0']
#
# genres = data['genres']
# ratings = data["content_rating"]
# scores = data["imdb_score"]
#
#
# totalGenres = list(set(genres))
# totalRatings = list(set(ratings))
#
# genreAssignedNumber = {}
# for i in range(len(totalGenres)):
#     genre = totalGenres[i]
#     genreAssignedNumber[genre] = i
#
# numberedGenreList = []
# for item in genres:
#     value = genreAssignedNumber[item]
#     numberedGenreList.append(value)
#
# ratingsAssignedNumber = {}
# for i in range(len(totalRatings)):
#     rating = totalRatings[i]
#     ratingsAssignedNumber[rating] = i
#
# numberedRatingList = []
# for item in ratings:
#     value = ratingsAssignedNumber[item]
#     numberedRatingList.append(value)
#
# data['NumberedGenre'] = numberedGenreList
# data['NumberedRating'] = numberedRatingList
#
#
# print(ratingsAssignedNumber)
# print(genreAssignedNumber)
#
# simplifiedScore = []
# for i in range(0, len(scores)):
#     rating = scores[i]
#     if rating <= 10 and rating >= 7.5:
#         simplifiedScore.append(4)
#     if rating >= 5 and rating <= 7.4:
#         simplifiedScore.append(3)
#     if rating >= 2.5 and rating <= 4.9:
#         simplifiedScore.append(2)
#     if rating >= 1 and rating <= 2.4:
#         simplifiedScore.append(1)
#
# data['SimpleScore'] = simplifiedScore
#
# cleaned_data = data
# cleaned_data.to_csv("movie_metadata_classfuy.csv",index =False)

data = pd.read_csv('movie_metadata_classfuy.csv', index_col=False)

"""
Get the target variables, the simple converted score
"""
targetDataSimpleScore = data['SimpleScore']

keep_col = ['duration', 'director_facebook_likes',
            'actor_1_facebook_likes', 'budget', 'title_year', 'movie_facebook_likes'
            ,'NumberedGenre','NumberedRating','SimpleScore']

"""
Get the Independent Variables
"""
independentVars = ['duration', 'director_facebook_likes',
            'actor_1_facebook_likes', 'budget', 'title_year', 'movie_facebook_likes'
            ,'NumberedGenre','NumberedRating']

new_data = data[keep_col]

independentVarsData = data[independentVars]

dataMatrix = new_data.as_matrix()

targetVariable = targetDataSimpleScore.as_matrix()
independentVariables = independentVarsData.as_matrix()

"""
Split the data, training and validating
split 50 50
Cross validation
"""
X_train, X_test, y_train, y_test = train_test_split(independentVariables,targetVariable,test_size=0.5,random_state=0)
X_train.shape, y_train.shape

X_test.shape, y_test.shape

"""
To preprocess data to standard scaler uncomment this
and change the X_test, y_test to transformed
"""
# scaler = preprocessing.StandardScaler().fit(X_train)
# X_train_transformed = scaler.transform(X_train)
#
# scaler2 = preprocessing.StandardScaler().fit(X_test)
# X_test_transformed = scaler.transform(X_test)

"""
Linear Regression
Accuracy: 21%
"""
linearRegression = linear_model.LinearRegression()
linearRegression.fit(X_train,y_train)
accuracyLinearR = linearRegression.score(X_test,y_test)
print(accuracyLinearR)
"""
Logistic Regression
Accuracy: 78%
"""
logisticRegression = linear_model.LogisticRegression()
logisticRegression.fit(X_train,y_train)
accuracyLogisticR = logisticRegression.score(X_test,y_test)
print(accuracyLogisticR)
"""
Support Vector Machine
Accuracy: 74%
"""
svmClf = svm.SVC(probability=True)
svmClf.fit(X_train,y_train)
svmAccuracy = svmClf.score(X_test,y_train)
print(svmAccuracy)
"""
Decision Tree Split on Entropy
Accuracy: 75%
Accuracy: 69% split on Gini
"""
decisionTree = tree.DecisionTreeClassifier(criterion="entropy")
decisionTree.fit(X_train,y_train)
decisionTreeAccur = decisionTree.score(X_test,y_test)
print(decisionTreeAccur)
"""
Guassian Naive
Accuracy: 44%
"""
gnb = GaussianNB()
gnb.fit(X_train,y_train)
gnbAccuracy = gnb.score(X_test,y_test)
print(gnbAccuracy)
"""
MultinomialNB
Accuracy: 25%
"""
mnb = MultinomialNB()
mnb.fit(X_train,y_train)
mnbAccuracy = mnb.score(X_test,y_test)
print(mnbAccuracy)
"""
Multi-Layer Perceptron (Neural Network Model)
Accuracy: 77%
Preprocessing: 80%
"""
mlp = MLPClassifier()
mlp.fit(X_train,y_train)
mlpAccuracy = mlp.score(X_test,y_test)
print(mlpAccuracy)


"""
Implement ROC curves later on
False Positive Rate vs True Positive Rate
"""


accuracy = [21,78,74,72,69,44,25,77]
models = ['linear reg', 'logistic reg', 'svm', 'DTree(Entropy)','DTree(Gini)', 'NB','MNB','MLP']
plt.figure(1)
plt.bar(range(len(accuracy)), accuracy, align='center')
plt.xticks(range(len(models)), models, size='small',rotation='vertical')
plt.ylabel("Accuracy")
plt.xlabel("Models")
plt.title("Model vs Accuracy")
plt.show()
































































