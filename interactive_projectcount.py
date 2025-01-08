
import pandas as pd 
import plotly.express as px

df = pd.read_csv('D:/ankita/python/carbon-market/2025_0103_1434.csv', sep='\t', encoding='utf-8')
print(df.head())


#Create the choropleth map
fig = px.choropleth(df, 
                    locations='ISO3',
                    locationmode='ISO-3',
                    color='COUNT', 
                    hover_name= 'COUNTRY',
                    hover_data= ['MARKET_TYPE', 'PROJECT_SCOPE', 'PROJECT_TYPE', 'TOTAL_CREDITS_ISSUED'],
                    title='Distribution of Project Types by Country')

# Display the figure
fig.show()