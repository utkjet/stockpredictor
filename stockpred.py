# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split

data = pd.read_csv(r'C:\Users\Utkarsh\Desktop\python\stock.csv')

x = data[["open", "high", "volume"]]
y = data["close"]

for i in range(1000):
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1)
    class_pred = linear_model.LinearRegression()
    class_pred.fit(x_train, y_train)
    pred = class_pred.predict(x_test)
    acc = class_pred.score(x_test,y_test)
    print("ACCURACY: " + str(acc*100) + "%")
    accmean += acc