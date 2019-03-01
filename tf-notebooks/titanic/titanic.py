# -*- coding: utf-8 -*- 
# @Time    : 19-3-1 上午10:14 
# @Author  : jayden.zheng 
# @FileName: titanic.py 
# @Software: PyCharm 
# @content :

import pandas as pd
import numpy as np
from pandas import Series,DataFrame

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)


import os
data_train = pd.read_csv(os.getcwd()+"/kaggleProject/titanic/data/train.csv")
"""
data_train.info()
data_train.describe()

"""