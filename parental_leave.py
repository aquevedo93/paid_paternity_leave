#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 22:27:50 2020

@author: andreaquevedo
"""


import pandas as pd 

family_leave= pd.read_csv("GENDER_EMP_28022020233243959.csv")

list(family_leave)


family_leave= family_leave[['Country', 'Indicator', 'Sex', 'Time', 'Value']]



family_leave.to_csv('family_leave_long.csv', index=False)



p_fl= pd.pivot_table(family_leave, values = 'Value', 
                     index='Country', 
                     columns = ['Indicator','Time', 'Sex']).reset_index()


p_fl.columns = [''.join(str(col)).strip() for col in p_fl.columns.values]


p_fl.to_csv('family_leave_wide.csv', index=False)
