# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:12:54 2024

@author: NANCY DAVID
"""

import pandas
file = pandas.read_csv("country_data.csv")
print(file)
print(file.info())
print(file.describe())


import pandas
file = pandas.read_csv("iris.csv")
print(file.info())
print(file.describe())


import pandas
file = pandas.read_csv("housing_data.csv")
print(file.info())
print(file.describe())

import pandas
file = pandas.read_csv("insurance_data.csv")
print(file.info())
print(file.describe())