# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 07:55:34 2022

@author: DELL
"""

archivo = 'dataset_s.csv'
import pandas as pd
import numpy as np
import csv
dt = pd.read_csv(archivo)

w = dt.Price.quantile([0.25,0.9,0.95])
x = dt.Rating.quantile([0.25,0.9,0.95])
print(w)
print(x)

