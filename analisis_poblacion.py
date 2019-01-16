#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:39:52 2019
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Centroides_NucleosPoblacion.csv")

print("El número de Municipios que tienen más de 100000 habitantes es", 
      len(data.groupby(['CodMun']).sum().loc[data.groupby(['CodMun']).sum() ["Poblacion"] > 100000]), ".\n")

plt.figure()
plt.figure(figsize=(20,10))
plt.bar(data["OBJECTID"], data["Poblacion"])
plt.xlabel('OBJECTID')
plt.ylabel('Población')
plt.xlim((1, len(data)))
plt.title('Población de cada ciudad') 
plt.show()
