import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

# Load the CSV file
df = pd.read_csv('AAV_Serotypes_PubMed_Search.csv')

# Create a Streamlit app
st.title('AAV Serotypes Publications Analysis')

# Plot the number of publications for each serotype over the given span of years using Plotly
st.header('Number of Publications for Each Serotype Over the Years')
fig = px.line(df, x='Year', y='Count', color='Keyword', title='Number of Publications for Each Serotype Over the Years')
st.plotly_chart(fig)

# Calculate the compound annual growth rate (CAGR) for each serotype
def calculate_cagr(first, last, periods):
    return (last / first) ** (1 / periods) - 1

cagr_data = []
for serotype in df['Keyword'].unique():
    serotype_data = df[df['Keyword'] == serotype]
    non_zero_data = serotype_data[serotype_data['Count'] > 0]
    first_year = non_zero_data.iloc[0]['Year']
    first_count = non_zero_data.iloc[0]['Count']
    last_year = non_zero_data.iloc[-1]['Year']
    last_count = non_zero_data.iloc[-1]['Count']
    periods = last_year - first_year
    cagr = calculate_cagr(first_count, last_count, periods)
    cagr_data.append((serotype, cagr))

cagr_df = pd.DataFrame(cagr_data, columns=['Serotype', 'CAGR'])

# Plot the CAGR for each serotype as a bar chart using Plotly
st.header('Compound Annual Growth Rate (CAGR) for Each Serotype')
fig2 = px.bar(cagr_df, x='Serotype', y='CAGR', title='Compound Annual Growth Rate (CAGR) for Each Serotype')
st.plotly_chart(fig2)
