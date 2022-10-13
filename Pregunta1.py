# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:49:44 2022

@author: DELL
"""

archivo = 'google_dataset.csv'
archivo2 = 'dataset_s.csv'
import pandas as pd
import random as rm
import csv
#dataset = pd.read_csv(archivo)
dataset2 = pd.read_csv(archivo2,sep=",")
print(dataset2)

#m = rm.sample(dataset,1000)
#m = sorted(dataset)
#print(m)


