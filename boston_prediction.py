#!/usr/bin/env python
# coding=utf-8

# fit a final xgboost model on the housing dataset and make a prediction
from numpy import asarray
from pandas import read_csv
import pandas as pd
from xgboost import XGBRegressor
# load the dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv'
dataframe = read_csv(url, header=None)
print(dataframe.info())
missing  = dataframe.isnull().sum()
print(missing)
data = dataframe.values
# split dataset into input and output columns
X, y = data[:, :-1], data[:, -1]
print(missing)
# define model
model = XGBRegressor()
# fit model
model.fit(X, y)
# define new data
row = [0.00632,18.00,2.310,0,0.5380,6.5750,65.20,4.0900,1,296.0,15.30,396.90,4.98]
new_data = asarray([row])
# make a prediction
yhat = model.predict(new_data)
# summarize prediction
print(f"Predicted {yhat}")
