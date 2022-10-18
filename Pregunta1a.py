# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:49:44 2022

@author: DELL
"""

archivo = 'dataset_s.csv'
import pandas as pd
import numpy as np

data = pd.read_csv("D:/Trabajos U/354/Examen1/dataset_s.csv", encoding='latin')

data.head

def percentil(per,x):
    n=len(x)
    pos=int((per*n)/100)
    aux=np.sort(x)
    return aux[pos]

#1ra columna
print("---------------1ra columna")
print(percentil(25, data.Price))
print(percentil(90, data.Price))
print(percentil(95, data.Price))
# 2da columna
print("---------------2da columna")
print(percentil(25, data.Rating))
print(percentil(90, data.Rating))
print(percentil(95, data.Rating))
# 3ra columna
print("------------3ra columna")
print(percentil(25, data['Maximum Installs']))
print(percentil(90, data['Maximum Installs']))
print(percentil(95, data['Maximum Installs']))
# 4ta columna
print("------------4ta columna")
print(percentil(25, data['Rating Count']))
print(percentil(90, data['Rating Count']))
print(percentil(95, data['Rating Count']))