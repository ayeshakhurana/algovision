import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():
    file_path = '/Users/ayesha/Downloads/algovision/algovision/Zepto_Analytics_Dataset (1).csv'
    df = pd.read_csv(file_path)  
    return df

df=load_data()

st.title('Zepto Analytics Dashboard')
st.subheader("Key Metrics")
st.metric("Total Orders", df['Customer_ID'].nunique())
st.metric("Total Revenue", f"${df['Price'].sum():,.2f}")
st.metric("Avg Delivery Time (min)", f"{df['Delivery_Time_mins'].mean():.2f}")

st.subheader("1. Optimizing Inventory and Reducing Stockouts")
fig=px.pie(df, names="Product_Category", title="Product Category Distribution")
st.plotly_chart(fig)
