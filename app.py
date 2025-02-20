import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the dashboard
st.title('Vehicle Data Dashboard')

#Load the dataset
df= pd.read_csv('vehicles_us.csv')

#Display dataset preview
st.write('### Dataset Preview', df.head())

# Add a checkbox to show the full dataset
if st.checkbox('Show Full Dataset'):
    st.write(df)
    
    # Header for the histogram
    st.header('Distribution of Vehicle Price')
    st.write('This histogram shows the  distribution of vehicle prices.')
    # Create a plotly histogram for the vehicle price
    st.write('### Distribution of Vehicle Price')
    fig_price = px.histogram(df, x='price', title='Vehicle Price Distribution')
    st.plotly_chart(fig_price)
    
    # Header for the scatter plot
    st.header('Price vs. Year by Condition')
    st.write('This scatter plot shows the how vehicle price varies by model year and condition.')
    # Create a Plotly scatter plot for the price vs model_year by the condition
    st.write('### Price vs. Year by Condition')
    fig_scatter = px.scatter(df, x='model_year', y='price', color='condition', title='Price vs Model Year by Condition')
    st.plotly_chart(fig_scatter) 
    
#Forcing github to update the file





    