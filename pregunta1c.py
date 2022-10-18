# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:24:08 2022

@author: DELL
"""

archivo = 'dataset_s.csv'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("D:/Trabajos U/354/Examen1/dataset_s.csv", encoding='latin')

data.head

w_installs = data['Maximum Installs']
x_price = data['Price']
y_rating = data['Rating']
z_count = data['Rating Count']

plt.title('Grafica Installs')
plt.plot(w_installs)
#plt.title('Grafica Price')
#plt.plot(x_price)
#plt.title('Grafica Rating')
#plt.plot(y_rating)
#plt.title('Grafica Count Rating')
#plt.plot(z_count)
plt.grid()
plt.show()