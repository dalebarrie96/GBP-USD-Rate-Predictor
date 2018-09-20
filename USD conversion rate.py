import pandas as pd
import math
import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression

#this gets the historical data into pandas df
df = pd.read_csv('GBP_USD_Historical_Data.csv')

#this calculates the high low percentage
df['HL_PCT'] = (df['High'] - df['Low']) / df['Low'] * 100.0
# this modifies the datafield with our own fields
df = df[['Price','Open','HL_PCT','Change %']]

#preprocessing was complaining about the % at the end of this column...
df['Change %'] = df['Change %'].str[:-1].astype(float)

predict_col = 'Price'

#drop all empty rows
df.dropna(inplace=True)

#this is how far forward we want to predict... with this data set its 
#nearly a month (27 days) math.ceil is just so we have a whole number
predict_out = int(math.ceil(0.01*len(df)))

#this is the label, it takes the column we want to predict and
#shifts it along as far as we want to predict
df['label'] = df[predict_col].shift(-predict_out)
df.dropna(inplace=True)
#print(df.head())

#x is going to be our features of the graph,
#so basically everything that isnt a prediction
x = np.array(df.drop(['label'],1))

#obv this is just the column i care about with prediction space
y= np.array(df['label'])

#this was just to check that they both are the same size (original - the predict_out)
#print(len(x), len(y))

#this trys to put all values between 1 and 0 (apparently it helps???)
x = preprocessing.scale(x)

#this splits my data set into features/labels and train and test values for me
#(doing 10% of my data should be roughly 1 year, should be enough)
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)

classifier = LinearRegression()

classifier.fit(x_train,y_train)

accuracy = classifier.score(x_test,y_test)

print(accuracy)


