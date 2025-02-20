import streamlit as st
import pandas as pd
import plotly.express as px
import os
# Title of the dashboard
st.title('Vehicle Data Dashboard')

#Load the dataset
df= pd.read_csv('vehicles_us.csv')

#Display dataset preview
st.write('### Dataset Preview', df.head())

# Add a checkbox to show the full dataset
if st.checkbox('Show Full Dataset'):
    st.write(df)
    
    # Create a plotly histogram for the vehicle price
    st.write('### Distribution of Vehicle Price')
    fig_price = px.histogram(df, x='price', title='Vehicle Price Distribution')
    st.plotly_chart(fig_price)
    
    # Create a Plotly scatter plot for the price vs model_year by the condition
    st.write('### Price vs. Year by Condition')
    fig_scatter = px.scatter(df, x='model_year', y='price', color='condition', title='Price vs Model Year by Condition')
    st.plotly_chart(fig_scatter)
    
    print("Current working directory:", os.getcwd())
    