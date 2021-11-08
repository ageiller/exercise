# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd 
import numpy as np
from joblib import memory
import os 

data = pd.DataFrame(np.random.normal(0,1,size = (1000,4)),columns = list('ABCD'))
os.getcwd()

os.chdir('/Users/antoine/Documents/git/data')

data.to_csv("database")

