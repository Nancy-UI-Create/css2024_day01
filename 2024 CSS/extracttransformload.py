# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:29:54 2024

@author: NANCY DAVID
"""

import pandas as pd

df = pd.read_csv("data_02/country_data_index.csv")

df = pd.read_csv("data_02/iris.csv")

"""
Absolute path: gives full location of the file
Located in C drive
D:/2024 CSS/2024 CSS/iris.csv 

Relative path: gives the exact location of the file
data_02/iris.csv

iris.csv
"""
import pandas as pd

df = pd.read_csv("data_02/country_data_index.csv")
print(df)
"""
Unnamed: 0  Age Gender       Country
0            0   39      M  South Africa
1            1   25      M      Botswana
2            2   29      F  South Africa
3            3   46      M  South Africa
4            4   22      F         Kenya
5            5   35      F    Mozambique
6            6   22      F       Lesotho
7            7   49      M         Kenya
8            8   30      M         Kenya
9            9   40      F         Egypt
10          10   30      M         Sudan
"""
import pandas as pd

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(df)
file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(file)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
file = pd.read_csv(url)

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)
