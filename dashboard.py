import streamlit as st
import pandas as pd

# Now we are loading the aggregated results
sales_per_product = pd.read_csv('sales_per_product')
daily_sales = pd.read_csv('daily_sales')

st.title('E-commerce Analytics Dashboard')

st.subheader('Top-Selling Products')
st.dataframe(sales_per_product.sort_values('total_sales', ascending=False).head(10))

st.subheader('Daily Sales Trend')
st.line_chart(daily_sales.set_index('price'))