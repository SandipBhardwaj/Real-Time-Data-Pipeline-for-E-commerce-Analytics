import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:901188@localhost:5432/Sandip')
# Load our clean data
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

orders = orders.merge(products[['product_id','name','category']], on='product_id', how='left')

# Total sales per product
sales_per_product = orders.groupby('name').agg({'price':'sum','order_id':'count'}).rename(columns={'order_id':'num_orders','price':'total_sales'})
print(sales_per_product.sort_values('total_sales',ascending=False).head())
sales_per_product.to_sql('sales_per_product', engine, if_exists='replace', index=True)
# Daily revenue trends
orders['timestamp'] = pd.to_datetime(orders['timestamp'])
daily_sales = orders.groupby(orders['timestamp'].dt.date)['price'].sum()
print(daily_sales.tail())

# Average order value
avg_order_value = orders.groupby('order_id')['price'].sum().mean()
print(f'Average order value:{avg_order_value}')

# Top user by user count
orders_per_user = orders.groupby('user_id')['order_id'].count().sort_values(ascending=False)
print(orders_per_user)