# Carbon Market Visualization Dashboard

![Dashboard Screenshot](

An interactive dashboard for visualizing carbon credit distribution across different project scopes and geographical regions.

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

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/carbon-market-visualization.git
cd carbon-market-visualization
```

## Usage
Run the application:
app.py

## Access the dashboard at:
http://localhost:8050

## Interact with the dashboard:
Use the dropdown to select project scopes
Hover over countries for detailed information
View automatic maximum credit annotations

## Acknowledgments
Built with Plotly Dash
Map data from Natural Earth
Plasma color scale by Plotly
