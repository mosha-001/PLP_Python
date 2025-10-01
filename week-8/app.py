import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
from wordcloud import WordCloud

import matplotlib.pyplot as plt

# -------------------------------
# Part 1: Data Loading & Exploration
# -------------------------------

# Load the data
def load_data():
    df = pd.read_csv("metadata.csv", low_memory=False)
    return df

df = load_data()


# Show basic info
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")
st.write("Sample of the data:")
st.dataframe(df.head())

# DataFrame dimensions
st.write(f"Shape of dataset: {df.shape}")

# Data types
st.write("Data types:")
st.write(df.dtypes)

# Missing values
st.write("Missing values per column:")
st.write(df.isnull().sum())

# Basic statistics for numerical columns
st.write("Basic statistics for numerical columns:")
st.write(df.describe())

# -------------------------------
# Part 2: Data Cleaning & Preparation
# -------------------------------

# Handle missing data
missing_threshold = 0.5
cols_to_drop = [col for col in df.columns if df[col].isnull().mean() > missing_threshold]
df_clean = df.drop(columns=cols_to_drop)

# Fill missing values in important columns
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
df_clean['journal'] = df_clean['journal'].fillna('Unknown')
df_clean['title'] = df_clean['title'].fillna('')

# Extract year
df_clean['year'] = df_clean['publish_time'].dt.year

# Abstract word count
df_clean['abstract_word_count'] = df_clean['abstract'].fillna('').apply(lambda x: len(str(x).split()))

# -------------------------------
# Part 3: Data Analysis & Visualization
# -------------------------------

# Interactive year range
min_year = int(df_clean['year'].min()) if not np.isnan(df_clean['year'].min()) else 2019
max_year = int(df_clean['year'].max()) if not np.isnan(df_clean['year'].max()) else 2022
year_range = st.slider("Select year range", min_year, max_year, (min_year, max_year))

df_filtered = df_clean[(df_clean['year'] >= year_range[0]) & (df_clean['year'] <= year_range[1])]

# Publications by year
year_counts = df_filtered['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index.astype(int), year_counts.values)
ax1.set_title('Publications by Year')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Publications')
st.pyplot(fig1)

# Top journals
top_journals = df_filtered['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax2)
ax2.set_title('Top 10 Journals')
ax2.set_xlabel('Number of Publications')
ax2.set_ylabel('Journal')
st.pyplot(fig2)

# Word cloud of titles
all_titles = ' '.join(df_filtered['title'].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

# Distribution by source_x (if exists)
if 'source_x' in df_filtered.columns:
    source_counts = df_filtered['source_x'].value_counts()
    fig4, ax4 = plt.subplots()
    sns.barplot(y=source_counts.index, x=source_counts.values, ax=ax4)
    ax4.set_title('Paper Counts by Source')
    ax4.set_xlabel('Number of Papers')
    ax4.set_ylabel('Source')
    st.pyplot(fig4)

# -------------------------------
# Part 4: Streamlit App Layout
# -------------------------------

st.write("Use the slider above to filter by publication year.")
st.write("You can explore the top journals, word cloud of titles, and paper counts by source.")

# Show a sample of the cleaned data
st.write("Sample of cleaned data:")
st.dataframe(df_filtered.head())

# -------------------------------
# Part 5: Documentation & Reflection
# -------------------------------

st.markdown("""
### Documentation & Reflection

- **Data Cleaning:** Dropped columns with >50% missing values, filled missing journals with 'Unknown', and handled missing titles/abstracts.
- **Analysis:** Explored publication trends, top journals, and common words in titles.
- **Visualizations:** Included bar charts and a word cloud for easy interpretation.
- **Challenges:** Handling missing dates and large text fields; Streamlit caching for performance.
- **Learning:** Gained experience with pandas, data cleaning, and building interactive Streamlit apps.
""")