import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setup
st.set_page_config(layout="wide", page_title="Netflix Data Visualization", page_icon=":tv:")
st.markdown("<h1 style='text-align: center; color: red;'>Netflix Data Visualization</h1>", unsafe_allow_html=True)
df = pd.read_csv('netflix_titles.csv')
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year
df['country'].fillna('Unknown', inplace=True)

# Sidebar Filters
type_filter = st.sidebar.multiselect('Select Type:', df['type'].unique(), default=df['type'].unique())
country_filter = st.sidebar.multiselect('Select Country:', df['country'].unique(), default=df['country'].unique())

filtered_df = df[df['type'].isin(type_filter) & df['country'].isin(country_filter)]

# Plot 1: Content Over Years
st.subheader("Content Added Over Years")
fig, ax = plt.subplots(figsize=(8,4))
filtered_df['year_added'].value_counts().sort_index().plot(kind='bar', color='red', ax=ax)
st.pyplot(fig)

# Plot 2: Type Split
st.subheader("Distribution of Type")
fig, ax = plt.subplots()
filtered_df['type'].value_counts().plot.pie(autopct='%1.1f%%', colors=['red', 'black'], ax=ax)
ax.set_ylabel('')
st.pyplot(fig)

# Plot 3: Top Countries
st.subheader("Top Countries in Selection")
fig, ax = plt.subplots(figsize=(8,4))
top_countries = filtered_df['country'].value_counts().head(10)
sns.barplot(y=top_countries.index, x=top_countries.values, color='red', ax=ax)
st.pyplot(fig)
