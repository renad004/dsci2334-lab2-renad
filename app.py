import streamlit as st
import pandas as pd

df = pd.read_csv('cafe_sales.csv')

st.title('☕ Qahwa Corner Sales Dashboard')


branches = df['branch'].unique()
selected_branch = st.selectbox('Select Branch', branches)

filtered_df = df[df['branch'] == selected_branch]


total_rev = filtered_df['total_sar'].sum()
st.metric(label="Total Revenue (SAR)", value=f"{total_rev:,.2f} SAR")


st.subheader('Revenue by Product')
product_revenue = filtered_df.groupby('product')['total_sar'].sum()
st.bar_chart(product_revenue)
