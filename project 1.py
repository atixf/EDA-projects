import pandas as pd

data = pd.read_csv('Ecommerce Purchases.csv ', index_col=0 )
print("DataFrame data:")
print(data)

#  display first 10 rows
print("\nFirst 10 rows of data:")
print(data.head(10))

#  display last 10 rows
print("\nLast 10 rows of data:")
print(data.tail(10))

#  check data types of each column
print("\nData types of each column:")
print(data.dtypes)

#  check for null values
print("\nChecking for null values in data:")
print(data.isnull().sum())

# count rows and columns
print("\nNumber of rows and columns in data:")
print(data.shape)

# heighest purchase price
print("\nHighest purchase price:")  
print(data['Purchase Price'].max())

# lowest purchase price
print("\nLowest purchase price:")
print(data['Purchase Price'].min())

# average purchase price
print("\nAverage purchase price:")
print(data['Purchase Price'].mean())

# check language of french
print("\nNumber of users with French as language:")
print(data[data['Language'] == 'fr']['Language'].count())

# check engineers
print("\nNumber of users with 'Engineer' as job title:")
print(data[data['Job'].str.contains('Engineer', case=False, na=False)]['Job'].count())

# find email of person with ip address 132.207.160.22
print(data[data['IP Address'] == '132.207.160.22']['Email'].values[0])

# how many people have master cards as credit card and made a purchase above 50
print("\nNumber of people with MasterCard and purchase above 50:")
print(data[(data['CC Provider'] == 'Mastercard') & (data['Purchase Price'] > 50)].shape[0])

# find the email of the person with the credit card number:4664825258997302
print("\nEmail of the person with credit card number 4664825258997302:")
print(data[data['Credit Card'] == 4664825258997302]['Email'].values[0])

# how many purchases on am and pm value count method
print("\nNumber of purchases made in AM and PM:")
print(data['AM or PM'].value_counts())

# how many people have a credit card expiring in 2020
print("\nNumber of people with credit cards expiring in 2020:")
print(data[data['CC Exp Date'].str.endswith('20')].shape[0])

# top 5 email providers
print("\nTop 5 email providers:")
print(data['Email'].str.split('@').str[1].value_counts().head(5))

