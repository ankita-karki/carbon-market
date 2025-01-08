import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('D:/ankita/python/carbon-market/2025_0103_1434.csv')

# Step 2: Display the first few rows of the DataFrame to understand its structure
print(df.head())

# Example 1: Bar Plot of Project Count by Market Type
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='MARKET_TYPE', y='PROJECT_COUNT', ci=None)
plt.title('Project Count by Market Type')
plt.xlabel('Market Type')
plt.ylabel('Project Count')
plt.show()

# Example 2: Heatmap of Total Credits Issued by Region and Market Type
heatmap_data = df.pivot_table(values='TOTAL_CREDITS_ISSUED', index='REGION', columns='MARKET_TYPE', aggfunc='sum')

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Total Credits Issued by Region and Market Type')
plt.xlabel('Market Type')
plt.ylabel('Region')
plt.show()

# Example 3: Count Plot of Unique Project Types by Region
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='REGION', hue='PROJECT_TYPE')
plt.title('Unique Project Types by Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.legend(title='Project Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Example 4: Scatter Plot of Total Credits Issued vs Project Count by Market Type
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='PROJECT_COUNT', y='TOTAL_CREDITS_ISSUED', hue='MARKET_TYPE', style='MARKET_TYPE')
plt.title('Total Credits Issued vs Project Count by Market Type')
plt.xlabel('Project Count')
plt.ylabel('Total Credits Issued')
plt.legend(title='Market Type')
plt.show()