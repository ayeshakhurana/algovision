import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():
    file_path = '/Users/ayesha/Downloads/algovision/algovision/Zepto_Analytics_Dataset (1).csv'
    df = pd.read_csv(file_path)  
    return df

df=load_data()

st.title('Zepto\'s Analytics Dashboard')
st.markdown("<h3 style='text-decoration: underline;'>Key Metrics</h3>", unsafe_allow_html=True)
st.metric("Total Orders", df['Customer_ID'].nunique())
st.metric("Total Revenue", f"${df['Price'].sum():,.2f}")
st.metric("Avg Delivery Time (min)", f"{df['Delivery_Time_mins'].mean():.2f}")

st.markdown("<h3 style='text-decoration: underline;'>Insights derived from the Dataset</h3>", unsafe_allow_html=True)

st.header("_1. Optimizing Inventory and Reducing Stockouts_")
fig=px.bar(df, x='Product_Category', title='Top Selling Products', y='Quantity',color='Product_Category',color_discrete_sequence=px.colors.qualitative.Set1)
st.plotly_chart(fig)

fig1=px.pie(df, names='Product_Category', title='Product Category Distribution')
st.plotly_chart(fig1)


st.markdown("""
### Exploratory data analysis (EDA) results

- **As we can see through the pie chart**, the top-selling products include **Dairy, Snacks, and Household Items**.
- **We can optimize inventory** by increasing stock of these products and reducing stock of less popular products such as **Beverages and Groceries**.**This will help** in reducing stockouts and increasing sales.
""")

st.header('_2.Enhance delievery time and meet 10 minute promise_')


fig=px.bar(df, x='City', title='Average Delivery Time by City', y='Delivery_Time_mins',color='City',color_discrete_sequence=px.colors.qualitative.Set1)
st.plotly_chart(fig)

fig=px.pie(df, names='Payment_Method', title='City-wise Order Distribution')

st.plotly_chart(fig)

fig=px.histogram(df, x='Gender', title='Delivery Time Distribution')
st.plotly_chart(fig)

fig = px.pie(df, 
             names='Payment_Method', 
             title='Most Opted Payment Method', 
             color_discrete_sequence=px.colors.qualitative.Set1,
             hole=0.4)
st.plotly_chart(fig)









