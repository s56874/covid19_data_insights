# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("COVID-19 Data Analysis Dashboard")

# Load CSV
data_path = "samarth_csv.csv"  # Make sure CSV is in the same folder
df = pd.read_csv(data_path)

# Convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar - Country selection
countries = df['Country/Region'].unique()
selected_country = st.sidebar.selectbox("Select Country", countries)

# Sidebar - Date range selection
min_date = df['Date'].min()
max_date = df['Date'].max()
start_date, end_date = st.sidebar.date_input(
    "Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date
)

# Filter data based on selections
filtered_df = df[
    (df['Country'] == selected_country) &
    (df['Date'] >= pd.to_datetime(start_date)) &
    (df['Date'] <= pd.to_datetime(end_date))
]

# Show metrics
confirmed = int(filtered_df['Confirmed'].sum())
deaths = int(filtered_df['Deaths'].sum())
recovered = int(filtered_df['Recovered'].sum())

# Get new cases from last row
new_confirmed = int(filtered_df['Confirmed'].diff().fillna(0).iloc[-1])
new_deaths = int(filtered_df['Deaths'].diff().fillna(0).iloc[-1])
new_recovered = int(filtered_df['Recovered'].diff().fillna(0).iloc[-1])

col1, col2, col3 = st.columns(3)
col1.metric("Confirmed", f"{confirmed:,}", f"+{new_confirmed:,} new")
col2.metric("Deaths", f"{deaths:,}", f"+{new_deaths:,} new")
col3.metric("Recovered", f"{recovered:,}", f"+{new_recovered:,} new")

# Trend over time
st.subheader("Trend Over Time")
trend_fig = px.line(
    filtered_df,
    x='Date',
    y=['Confirmed', 'Deaths', 'Recovered'],
    labels={'value':'Count','variable':'Status'},
    title=f"COVID-19 Trend in {selected_country}"
)
st.plotly_chart(trend_fig, use_container_width=True)

# Top 10 countries by confirmed cases
st.subheader("Top 10 Countries by Confirmed Cases")
latest_data = df[df['Date'] == df['Date'].max()]
top10 = latest_data.groupby('Country')['Confirmed'].sum().sort_values(ascending=False).head(10).reset_index()
bar_fig = px.bar(top10, x='Country', y='Confirmed', title="Top 10 Countries by Confirmed Cases")
st.plotly_chart(bar_fig, use_container_width=True)

# Global map
st.subheader("Global Map of Confirmed Cases")
map_fig = px.choropleth(
    latest_data,
    locations="Country",
    locationmode="country names",
    color="Confirmed",
    hover_name="Country",
    color_continuous_scale="Reds",
    title="Global COVID-19 Confirmed Cases"
)
st.plotly_chart(map_fig, use_container_width=True)
