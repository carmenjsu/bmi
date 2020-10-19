# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:28:20 2020

@author: CSu
"""

class calculator: 
    
    def __init__ (self):
        import pandas as pd
        import datetime as date 
        
        self.df_input = pd.read_csv('../Inputs.csv',sep='\s*,\s*') 
        self.df = pd.DataFrame()
        self.today = date.date.today().strftime("%Y%m%d")

    def inputs (self):
        return self.df_input['name']

    def bmi (self):
        return self.df_input['weight(kg)']/(self.df_input['hight(m)']**2)

    def classification (self, col):
        import numpy as np
        self.conditions = [
                    (col < 18.50),
                    (col >= 18.50) & (col < 25.00),
                    (col >= 25.00) & (col < 30.00),
                    (col >= 30.00) & (col < 35.00),
                    (col >= 35.00) & (col < 40.00),
                    (col >= 40.00)]
        self.choices = ['Underweight', 'Normal Weight', 'Overweight','Class I Obesity','Class II Obesity','Class III Obesity']
        return np.select(self.conditions, self.choices, default='null')

    def output(self):
        self.df.to_csv(r'../results/Results_{}.csv'.format(self.today), index=False)

    # execution 
    def calculator (self):        
        self.df['Name'] = self.inputs()
        self.df['BMI'] = self.bmi()    
        self.df['Classification'] = self.classification(self.df['BMI'])
        self.output()