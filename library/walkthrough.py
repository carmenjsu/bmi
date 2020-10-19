# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:30:39 2020

@author: CSu
"""

import pandas as pd 
import numpy as np
# read inputs, sep='\s*,\s*' to take care space in column names
df_input = pd.read_csv('Inputs.csv',sep='\s*,\s*') 


df = pd.DataFrame()
# object name
df['Name'] = df_input['name']


# do the BMI calculation 
df['BMI'] = df_input['weight(kg)']/(df_input['hight(m)']**2)


# classify per BMI
conditions = [
    (df['BMI'] < 18.50),
    (df['BMI'] >= 18.50) & (df['BMI'] < 25.00),
    (df['BMI'] >= 25.00) & (df['BMI'] < 30.00),
    (df['BMI'] >= 30.00) & (df['BMI'] < 35.00),
    (df['BMI'] >= 35.00) & (df['BMI'] < 40.00),
    (df['BMI'] >= 40.00)]
choices = ['Underweight', 'Normal Weight', 'Overweight','Class I Obesity','Class II Obesity','Class III Obesity']

df['Classification'] = np.select(conditions, choices, default='null')
    
# output the results  
df.to_csv('Results.csv', index=False)
