# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 07:55:34 2022

@author: DELL
"""

archivo = 'dataset_s.csv'
import pandas as pd

data = pd.read_csv("D:/Trabajos U/354/Examen1/dataset_s.csv", encoding='latin')

w = data.Price.quantile([0.25,0.9,0.95])
x = data.Rating.quantile([0.25,0.9,0.95])
y = data['Maximum Installs'].quantile([0.25,0.9,0.95])
z = data["Rating Count"].quantile([0.25,0.9,0.95])

#data.columns
print("---------------1ra columna")
print(w)
print("---------------2da columna")
print(x)
print("---------------3ra columna")
print(y)
print("---------------4ta columna")
print(z)

