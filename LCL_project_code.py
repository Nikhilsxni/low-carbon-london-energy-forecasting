# -*- coding: utf-8 -*-
"""
Created on Wed Jun 7 19:49:27 2024

@author: Nikhil Soni
"""

import pandas as pd

# Load dataset
df = pd.read_csv("C:\Data Science Project\LCL-June2015v2_0.csv")
df['DateTime'] = pd.to_datetime(df['DateTime'])
# Display basic information about the dataset
print(df.info())
print(df.describe())

# Check for missing values
print(df.isnull().sum())

