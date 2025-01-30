#  Carbon Market Visualization Dashboard

![Dashboard Screenshot](https://github.com/ankita-karki/carbon-market/blob/main/output%20map/Forestry&Landuse.png?raw=true)

This repository contains an interactive dashboard for visualizing carbon credit distribution across different project scopes and geographical regions.The dataset used in this project was obtained from SQL queries run on carbon market registries.

Data Source

The dataset includes aggregated project data from multiple voluntary carbon market registries, processed through SQL queries. The extracted data consists of:
* Region
* Country
* Market Type
* Project Scope
* Project Type
* Total Credits Issued
* Number of Projects

## Features

- **Interactive Choropleth Map**: Visualize credit distribution across countries
- **Project Scope Filtering**: Dropdown selector for different project categories
- **Real-time Insights**:
  - Automatic detection of region with highest credits
  - Annotated maximum value display
- **Detailed Tooltips**: 
  - Total credits issued
  - Number of projects per country
- **Responsive Design**: Adapts to different screen sizes

## Prerequisites

- Python 3.7+
- Required packages:
  - pandas
  - dash
  - plotly
- Data file: `2025_0103_1434.csv` (tab-separated, UTF-8 encoded)


## Access the dashboard at:
http://127.0.0.1:8050/


## Interact with the dashboard:
Use the dropdown to select project scopes
Hover over countries for detailed information
View automatic maximum credit annotations

## Acknowledgments
Built with Plotly Dash
Map data from Natural Earth
Plasma color scale by Plotly
