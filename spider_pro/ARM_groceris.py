# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:36:59 2019..

@author: Hari
"""

import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import association_rules,apriori

df = pd.read_csv('c:/Users/Hari/Desktop/datasets/Naresh_datasets/groceries_200.csv')

df.isnull().sum()
df.fillna(0,inplace=True)

df.isnull().sum()

arr = np.array(df.values)

len(arr)
len(df)

all_items = np.unique(arr[~(arr==0)])

basket = pd.DataFrame(0,index=np.arange(len(arr)),columns=all_items)


for col in df.columns:
    t_f = (df[col].values != 0)
    itmes = df.iloc[t_f,col]
    indx = itmes.index
    
    for i in range(len(itmes)):
        basket.loc[indx[i]][itmes[i]] +=1