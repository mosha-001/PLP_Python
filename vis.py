import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
# %% Task 1: Load dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))

    print(df.head(), "\n")
    print(df.info(), "\n")
    print(df.isnull().sum())
except Exception as e:
    print("Error:", e)

# %% Task 2: Basic analysis
print(df.describe(), "\n")
print(df.groupby('species')['petal length (cm)'].mean(), "\n")

# %% Task 3: Visualizations
sns.set(style="whitegrid")

# Line chart
df['petal length (cm)'].expanding().mean().plot(figsize=(8,5))
plt.title("Cumulative Mean Petal Length")
plt.show()

# Bar chart
sns.barplot(data=df, x='species', y='sepal length (cm)', ci=None)
plt.title("Average Sepal Length by Species")
plt.show()

# Histogram
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Sepal Width Distribution")
plt.show()

# Scatter plot
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Sepal vs Petal Length")
plt.show()