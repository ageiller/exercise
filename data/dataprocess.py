#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:36:20 2021

@author: antoine
"""

import pandas as pd 
import os 

path = os.getcwd()

df = pd.read_csv('database', index_col = 0)

df.A[df.A>0]