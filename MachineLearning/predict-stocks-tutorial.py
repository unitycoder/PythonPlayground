# stocks prediction example
# source until to page https://pythonprogramming.net/forecasting-predicting-machine-learning-tutorial/

import quandl, math
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

df = quandl.get("WIKI/GOOGL")

# pair down our original dataframe
df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]

# transform our data
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0

# add daily percent change column
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# define a new dataframe as
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

print(df.head())


# add new rows 
forecast_col = 'Adj. Close'
# define the forecasting column, then we fill any NaN data with -99999
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))

# We'll assume all current columns are our features, so we'll add a new column with a simple pandas operation
df['label'] = df[forecast_col].shift(-forecast_out)

# standard with machine learning in code to define X (capital x) # as the features,
# and y (lowercase y) as the label that corresponds to the features
X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

# drop any still NaN information from the dataframe
df.dropna(inplace=True)

y = np.array(df['label'])

# Generally, you want your features in machine learning to be in a range of -1 to 1
#X = preprocessing.scale(X)

# create the label, y
y = np.array(df['label'])

# Now comes the training and testing
# The way this works is you take, for example, 75% of your data,
# and use this to train the machine learning classifier.
# Then you take the remaining 25% of your data, and test the classifier
# the return here is the training set of features, testing set of features,
# training set of labels, and testing set of labels
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

# define our classifier, for now, let's use Support Vector Regression from Scikit
#clf = svm.SVR()
# Let's try another classifier, if get better results
# n_jobs=-1 means, use threading, all cores
clf = LinearRegression(n_jobs=-1)

# Once you have defined the classifer, you're ready to train it
# we're "fitting" our training features and training labels
clf.fit(X_train, y_train)

# Our classifier is now trained, can test it
confidence = clf.score(X_test, y_test)

#print(confidence)

# try different kernels
#for k in ['linear','poly','rbf','sigmoid']:
#    clf = svm.SVR(kernel=k)
#    clf.fit(X_train, y_train)
#    confidence = clf.score(X_test, y_test)
#    print(k,confidence)

# predict
forecast_set = clf.predict(X_lately)

print(forecast_set, confidence, forecast_out)

# visualize
style.use('ggplot')

# add a new column to our dataframe, the forecast column
df['Forecast'] = np.nan

# predict 1 day ahead
last_date = df.iloc[-1].name
last_unix = last_date.timestamp() # FIXME: doesnt work in python 2.x
one_day = 86400
next_unix = last_unix + one_day

# add the forecast to the existing dataframe
for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

# build graph
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
