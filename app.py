import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Supermarket Sales Data')

df = pd.read_csv('supermarket.csv')

sorted_df = df.sort_values(by='store_sales', ascending=False)

top_10_stores = sorted_df.head(10)

total = df['store_sales'].sum()
formatted_total = "${:,.2f}".format(total)
st.header(f'Total Amount of Sales is {formatted_total}')

top_10_stores_df = pd.DataFrame({'store_sales': top_10_stores['store_sales'].values}, index=top_10_stores['store_id'])

show_customer_count = st.checkbox("Show Customer Count")

if show_customer_count:
    customer_count_df = pd.DataFrame({'store_id': top_10_stores['store_id'], 'daily_customer_count': top_10_stores['daily_customer_count']})
    plt.figure(figsize=(10, 6))
    plt.scatter(customer_count_df['store_id'], customer_count_df['daily_customer_count'])
    plt.xlabel('Store ID')
    plt.ylabel('Number of Customers')
    plt.title('Number of Customers in Top 10 Stores')
    plt.grid(True)
    st.pyplot()

st.subheader("Top 10 Stores based on Sales:")
st.bar_chart(top_10_stores_df)