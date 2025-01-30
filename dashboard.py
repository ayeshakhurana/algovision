import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():
    file_path = '/Users/ayesha/Downloads/algovision/algovision/Zepto_Analytics_Dataset (1).csv'
    df = pd.read_csv(file_path)  
    return df

df=load_data()

st.title('Zepto Analytics Dashboard')

