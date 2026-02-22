#  Carbon Market Analysis: Data Processing & Visualization Dashboard

![Dashboard Screenshot](https://github.com/ankita-karki/carbon-market/blob/main/output%20map/Forestry&Landuse.png?raw=true)

This repository provides SQL scripts for cleaning, transforming, and analyzing carbon credit project data from major registries, including VCS (Verra), Gold Standard (GS), American Carbon Registry (ACR), and Climate Action Reserve (CAR). The processed data is aggregated and visualized through an interactive dashboard, showcasing carbon credit distribution by project scope and geographic region. All datasets used in this project were generated from SQL queries executed on carbon market registries.

## Data Source
The dataset includes aggregated project data from multiple voluntary carbon market registries (VCS, GS, ACR, CAR), processed through SQL queries. The extracted data consists of:
* Region
* Country
* Market Type
* Project Scope
* Project Type
* Total Credits Issued
* Number of Projects


## SQL Query Functionality
The SQL query performs the following operations:
1. Combines data from all four registries using UNION ALL.
2. Standardizes column names to ensure consistency across registries.
3. Groups data by region, country, market type, project scope, and project type.
4. Counts the number of projects in each group.
5. Sorts results by region, country, market type, and project count in descending order.


## Visualization Features

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
https://musical-lamp-pj7rv4rw9v4x27jxj-8501.app.github.dev/


## Interact with the dashboard:
Use the dropdown to select project scopes
Hover over countries for detailed information
View automatic maximum credit annotations

## Acknowledgments
Built with Plotly Dash
Map data from Natural Earth
Plasma color scale by Plotly
