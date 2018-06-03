#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:29:26 2018

@author: Shashank Pawar
Simple Linear Regression
"""


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# SLR on training set
from sklearn.linear_model import LinearRegression
slr = LinearRegression()
slr.fit(X_train,y_train)

# Testing the SLR model
y_pred = slr.predict(X_test)

# Visulizing the results
sc1 = plt.scatter(X_train, y_train, color='red', marker = '.')
sc2 = plt.scatter(X_test, y_test, color='green', marker = '*')
line = plt.plot(X_train,slr.predict(X_train), color = 'blue')
plt.legend((sc1,sc2),('Training Samples', 'Testing Samples'))
plt.title('Test Results')
plt.xlabel('Years of experience')
plt.ylabel('Salary ($)')
plt.show()
