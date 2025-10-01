import pandas as pd

# First we will load our data

users = pd.read_csv('users.csv')
products = pd.read_csv('products.csv')
orders = pd.read_csv('orders.csv')

# Now we will remove all duplicates from our CSV files

users = users.drop_duplicates(subset='user_id')
products = products.drop_duplicates(subset='product_id')
orders = orders.drop_duplicates(subset='order_id')

# Now we will handle all missing values

users = users.dropna(subset=['email'])
products = products.fillna({'category': 'Unknown','price':0})
orders = orders.dropna()

# Now we will Fix its Data Types

users['signup_date'] = pd.to_datetime(users['signup_date'])
products['timestamp'] = pd.to_datetime(orders['timestamp'])
products['price'] = pd.to_numeric(products['price'])

# Examples enrichment: adding products name/category to orders
orders = orders.merge(products[['product_id','name','category']], on='product_id', how='left')

print(orders.head())