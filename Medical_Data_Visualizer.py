import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# import data
df = pd.read_csv('medical_examination.csv')

## Task 1: Add an overweight column to the data. 
#          To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters.
#          If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.

#convert height into meters
height_in_m = df['height'] * 0.01

#calculate bmi and create new column
bmi = round((df['weight'] / (height_in_m)**2), 0)
df['overweight'] = bmi

#replace bmi values with either 1 or 0
df['overweight'] = np.where(df['overweight'] <= 25, 0, 1)

## Task 2: Normalize the data by making 0 always good and 1 always bad. If the value of
#          cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.
           
df['cholesterol'] = np.where(df['cholesterol'] > 1, 0, 1)
df['gluc'] = np.where(df['gluc'] > 1, 0, 1)


## Task 3: Convert the data into long format and create a chart that shows the value counts
#          of the categorical features using seaborn's catplot(). The dataset should be split 
#           by 'Cardio' so there is one chart for each cardio value. 
#           The chart should look like examples/Figure_1.png.


