# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:19:59 2022

@author: DELL
"""
import pandas as pd
import numpy as np

dt = pd.read_csv("D:/Trabajos U/354/Examen1/dataset_s.csv", encoding='latin')

def media(x):
    sum=np.mean(x)
    #n=len(x)
    #res =sum/n
    return sum

def varianza (x):
    aux = sum(x**2)
    n=len(x)
    res= aux/n-media(x)
    return res
def desv_st(x):
    res=np.sqrt(varianza(x))
    return res

print("Price-------------------")
print(media(dt.Price))
print(varianza(dt.Price))
print(desv_st(dt.Price))

print("Installs-------------")
print(dt['Maximum Installs'].describe())

#tabla de frecuencias para datos booleanos
tab=pd.crosstab(index=dt['Free'],columns="count")
print(tab/tab.sum())
