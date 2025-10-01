import pandas as pd

# We will read our Raw data which is present in Our CSV files

users = pd.read_csv('users.csv')
products = pd.read_csv('products.csv')
orders = pd.read_csv('orders.csv')

print(users.head())
print(products.head())
print(orders.head())