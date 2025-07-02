import pandas as pd
import numpy as np

dict1 ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv',
                'Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male',
                         'Female','Female']
               }
df1=pd.DataFrame(dict1)

print("DataFrame df1:")
print(df1)

# displat first 3 rows
print("\nFirst 3 rows of df1:")
print(df1.head(3))

# display last 3 rows
print("\nLast 3 rows of df1:") 
print(df1.tail(3))

# shape of the DataFrame
print("\nShape of df1:")
print(df1.shape)

# information about the DataFrame
print("\nInformation about df1:")
print(df1.info())

# check for null values
print("\nChecking for null values in df1:")
print(df1.isnull().sum())

# descriptive statistics
print("\nDescriptive statistics of df1:")
print(df1.describe(include='all'))

# display unique values in gender column
print("\nUnique values in gender column:")
print(df1['Gender'].unique())

# number of unique values in gender column
print("\nNumber of unique values in gender column:")
print(df1['Gender'].nunique())

# count of unique values in gender column
print("\nCount of unique values in gender column:")
print(df1['Gender'].value_counts())

# total students having marks greater than 90 using between method
print("\nTotal students having marks greater than 90 using between method:")
print((df1[df1['Marks'].between(90, 100)]))

# average marks of all students
print("\nAverage marks of all students:")
print(df1['Marks'].mean())

# apply function to calculate percentage
def calculate_percentage(marks):
    return marks / 100 * 100

df1['Percentage'] = df1['Marks'].apply(calculate_percentage)
print("\nDataFrame df1 after adding Percentage column:")
print(df1)

# drop the Percentage column
df1.drop(columns=['Percentage'], inplace=True)
print("\nDataFrame df1 after dropping Percentage column:")
print(df1)

# add a new column 'Passed' based on marks
def check_passed(marks):
    return 'Passed' if marks >= 40 else 'Failed' 
df1['Passed'] = df1['Marks'].apply(check_passed)
print("\nDataFrame df1 after adding Passed column:")
print(df1)

# print column names
print("\nColumn names in df1:")
print(df1.columns.tolist())

# sort DataFrame by Marks in descending order
df1_sorted = df1.sort_values(by='Marks', ascending=False)
print("\nDataFrame df1 sorted by Marks in descending order:")
print(df1_sorted)

#  display name and marks of female students
print("\nName and Marks of female students:")
print(df1[df1['Gender'] == 'Female'][['Name', 'Marks']])

