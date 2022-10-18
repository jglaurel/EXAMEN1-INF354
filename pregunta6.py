# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:45:28 2022

@author: DELL
"""

import pandas as pd
import numpy as np
from numpy import nan as NA
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv("D:/Trabajos U/354/Examen1/dataset_s.csv", encoding='latin')

#df.pop('Category')
df.pop('App Name')
df.pop('App Id')
df.pop('Installs')
df.pop('Size')
df.pop('Minimum Android')
df.pop('Currency')
df.pop('Developer Id')
df.pop('Released')
df.pop('Last Updated')
df.pop('Content Rating')
df.pop('Developer Website')
df.pop('Developer Email')
df.pop('Privacy Policy')
df.pop('Scraped Time')

#eliminar datos NA
df.dropna()

df=pd.get_dummies(data=df, drop_first=True)

print(df.sample(10))
explicativas=df.drop(columns='Category')
objetivo=df['Category']

model=DecisionTreeClassifier(max_depth=3)
model.fit(X=explicativas,y=objetivo)
DecisionTreeClassifier()

plot_tree(decision_tree=model,feature_names=explicativas.columns,filled=True,fontsize=8)
plt.figure(figsize=(14,8))
