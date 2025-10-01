# analysis.py
# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Step 2: Load dataset (make sure metadata.csv is in the same folder)
df = pd.read_csv("metadata.csv", low_memory=False)

# Step 3: Explore dataset
print("Shape of dataset:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum().head(20))
print("\nSample rows:")
print(df.head())

# Step 4: Clean data
# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Drop rows with no publish_time
df = df.dropna(subset=['publish_time'])

# Extract year
df['year'] = df['publish_time'].dt.year

# Add abstract word count
df['abstract_word_count'] = df['abstract'].astype(str).apply(lambda x: len(x.split()))

# Step 5: Analysis
# Papers per year
year_counts = df['year'].value_counts().sort_index()
print("\nPapers per year:\n", year_counts)

# Top journals
top_journals = df['journal'].value_counts().head(10)
print("\nTop journals:\n", top_journals)

# Word frequency in titles
all_titles = " ".join(df['title'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_titles)

# Step 6: Visualizations
plt.figure(figsize=(10, 5))
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis")
plt.title("Top Journals Publishing COVID-19 Research")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.show()

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Paper Titles", fontsize=16)
plt.show()

plt.figure(figsize=(10, 5))
df['source_x'].value_counts().head(10).plot(kind="bar")
plt.title("Top Sources")
plt.xlabel("Source")
plt.ylabel("Count")
plt.show()
