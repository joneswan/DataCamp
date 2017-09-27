# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 00:06:19 2017

@author: jwan
"""

# Import the `pandas` library as `pd`
import pandas as pd

# Load in the data with `read_csv()`
digits_tra = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra", header=None)
digits_tes = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tes", header=None)

# Print out `digits`
print(digits_tra)
print(digits_tes)