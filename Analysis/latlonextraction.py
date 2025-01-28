import pandas as pd
import plotly.express as px

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('D:/ankita/python/carbon-market/2025_0103_1434.csv', sep = '/t')
print(df.head())
print(df.columns)


df['COUNT'] = df['COUNT'].fillna(0)
df['ISO3'] = df['ISO3'].fillna('Unknown')


# Create the choropleth map
fig = px.choropleth(df, 
                    locations='ISO3',
                    locationmode='ISO-3',
                    color='COUNT', 
                    hover_name= 'COUNTRY',
                    hover_data= ['MARKET_TYPE', 'PROJECT_SCOPE', 'PROJECT_TYPE', 'TOTAL_CREDITS_ISSUED'],
                    title='Project Count by Country')

# Display the figure
fig.show()

