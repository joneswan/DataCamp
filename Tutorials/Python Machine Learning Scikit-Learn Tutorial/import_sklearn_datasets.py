# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:46:42 2017

@author: jwan
"""

# Import `datasets` from `sklearn`
from sklearn import datasets

# Load in the `digits` data
digits = datasets.load_digits()

# Print the `digits` data 
print(digits)

# Note it can also be done as below
# import sklearn.datasets
# digits = sklearn.datasets.load_digits()
