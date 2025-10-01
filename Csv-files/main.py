from faker import Faker
import pandas as pd
import random

# First we will initialize our Faker
fake = Faker()
NUM_USERS = 500
NUM_PRODUCTS = 100
NUM_ORDERS = 1000

# Now we will generate Users
data_users = []
for i in range(1,NUM_USERS + 1):
    data_users.append({
        'user_id' : i,
        'name' : fake.name(),
        'email': fake.email(),
        'signup_date': fake.date_between(start_date='-2y', end_date='today')
    })
df_users = pd.DataFrame(data_users)
df_users.to_csv('users.csv', index=False)

# Now we will generate Products
categories = ['Electronics','Clothing','Books','Sports','Home','Beauty']
data_products = []
for i in range(1, NUM_PRODUCTS + 1):
    data_products.append({
        'product_id':i,
        'name' : fake.word().capitalize() + " " + random.choice(['Pro','Lite','X','Max','Plus']),
        'category' :random.randint(0,500),
        'price' : round(random.uniform(10,1000), 2)
    })
df_products = pd.DataFrame(data_products)
df_products.to_csv('products.csv', index=False)

# Now we will be generating Orders
order_data = []
for i in range(1, NUM_ORDERS + 1):
    product = random.choice(data_products)
    user = random.choice(data_users)
    order_data.append({
        'order_id' : i,
        'user_id' : user['user_id'],
        'product_id': product['product_id'],
        'quantity': random.randint(1,5),
        'price': product['price'],
        'timestamp' : fake.date_time_between(start_date=user['signup_date'], end_date='now')
    })
df_orders = pd.DataFrame(order_data)
df_orders.to_csv('orders.csv', index=False)