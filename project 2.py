import pandas as pd
import numpy as np

salary_data = pd.read_csv('Salaries.csv', index_col=0)
print("DataFrame salary_data:")
print(salary_data)

# columns in the DataFrame
print("\nColumns in salary_data:")
print(salary_data.columns)

# get info about the DataFrame
# print("\nInformation about salary_data:")
# print(salary_data.info())

# check for null values
print("\nChecking for null values in salary_data:")
print(salary_data.isnull().sum())

# drop id, notes, agency, and status columns
# salary_data.drop(columns=['Notes', 'Agency', 'Status'], inplace=True)
# print the DataFrame after dropping columns
# print("\nDataFrame salary_data after dropping Notes, Agency, and Status columns:")
# print(salary_data)

#  get statistics of all columns
# print("\nStatistics of all columns in salary_data:")
# print(salary_data.describe(include='all')) 

# top 5 occurrences of employee names
# print("\nTop 5 occurrences of employee names:") 
# print(salary_data['EmployeeName'].value_counts().head(5))

#  number of unique job titles
# print("\nNumber of unique job titles:")
# print(salary_data['JobTitle'].nunique())

# total number of job titles that contain 'captain'
# captain_count = salary_data['JobTitle'].str.contains('captain', case=False, na=False).sum()
# print("\nTotal number of job titles that contain 'captain':")
# print(captain_count)

# employee names from the 'Fire Department' 
# fire_department_employees = salary_data[salary_data['JobTitle'].str.contains('Fire', case=False, na=False)]['EmployeeName']
# print("\nEmployee names from the 'Fire Department':")
# print(fire_department_employees)

# minimum and maximum and average base salary
# print("\nMinimum, maximum, and average base salary:")
# print(salary_data['BasePay'].describe())

# replace 'Not Provided' with NaN in employee name
#  df[col] = df[col].method(value)
# 'df.method({col: value}, inplace=True)'

salary_data['EmployeeName'].replace('Not Provided', np.nan, inplace=True)
# print the DataFrame after replacing 'Not Provided' with NaN
print("\nDataFrame salary_data after replacing 'Not Provided' with NaN in EmployeeName:")
print(salary_data)

# drop rows with 3 missing values
# salary_data.drop(salary_data[salary_data.isnull().sum(axis=1) == 3].index, inplace=True)
# print the DataFrame after dropping rows with 3 missing values
# print("\nDataFrame salary_data after dropping rows with 5 missing values:")
# print(salary_data)

# find job title of ALBERT PARDINI
albert_pardini_job_title = salary_data[salary_data['EmployeeName'] == 'ALBERT PARDINI']['JobTitle']
print("\nJob title of ALBERT PARDINI:")
print(albert_pardini_job_title)

# how much ALBERT PARDINI earns including benefits
albert_pardini_salary = salary_data[salary_data['EmployeeName'] == 'ALBERT PARDINI']['TotalPayBenefits']
print("\nTotal pay and benefits of ALBERT PARDINI:")
print(albert_pardini_salary)

# name of the employee with the highest total pay
highest_total_pay_employee = salary_data.loc[salary_data['TotalPayBenefits'].idxmax()]['EmployeeName']
print("\nName of the employee with the highest total pay:")
print(highest_total_pay_employee)


# convert not provided to NaN in BasePay
salary_data['BasePay'].replace('Not Provided', np.nan, inplace=True)
# convert BasePay to numeric
salary_data['BasePay'] = pd.to_numeric(salary_data['BasePay'], errors='coerce')

# find average base pay of all employees per year
average_base_pay_per_year = salary_data.groupby('Year')['BasePay'].mean()
print("\nAverage base pay of all employees per year:")
print(average_base_pay_per_year)

# find average base pay of all employees per job title
average_base_pay_per_job_title = salary_data.groupby('JobTitle')['BasePay'].mean().sort_values(ascending=False)
print("\nAverage base pay of all employees per job title:")
print(average_base_pay_per_job_title)

# average base pay of employees with job title accountant
accountant_base_pay = salary_data[salary_data['JobTitle'].str.contains('Accountant', case=False, na=False)]['BasePay'].mean()
print("\nAverage base pay of employees with job title 'Accountant':")
print(accountant_base_pay)

# 5 most common job titles
most_common_job_titles = salary_data['JobTitle'].value_counts().head(5)
print("\n5 most common job titles:")
print(most_common_job_titles)