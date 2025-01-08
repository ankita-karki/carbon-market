import pandas as pd
import folium
import plotly.express as px
from folium.plugins import MarkerCluster
from folium.features import DivIcon

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('D:/ankita/python/carbon-market/2025_0103_1434.csv')


# Step 2: Aggregate the data as needed
country_data = df.groupby(['country', 'market_type']).agg({
    'project_count': 'sum',
    'total_credits_issued': 'sum'
}).reset_index()

# Step 3: Create the base map
m = folium.Map(location=[20, 0], zoom_start=2)

# Step 4: Add the project markers
marker_cluster = MarkerCluster().add_to(m)

for idx, row in country_data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],  # You need to have latitude and longitude for each country
        popup=f"Country: {row['country']}<br>Market Type: {row['market_type']}<br>Project Count: {row['project_count']}<br>Total Credits Issued: {row['total_credits_issued']}",
        icon=folium.Icon(color='blue' if row['market_type'] == 'VCS' else 'green'),
    ).add_to(marker_cluster)

# Step 5: Create the interactive legend with Plotly
fig = px.scatter_geo(country_data, locations="country", locationmode="country names",
                     size="project_count", color="market_type",
                     hover_name="country", hover_data=["project_count", "total_credits_issued"],
                     projection="natural earth")

fig.update_layout(title='Project Types and Emission Reductions by Country',
                  geo=dict(showframe=False, showcoastlines=True))

# Save the map to an HTML file
m.save('interactive_map.html')

# Display the Plotly figure
fig.show()