import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('D:/ankita/python/carbon-market/2025_0103_1434.csv', sep='\t', encoding='utf-8')

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Carbon Market Visualization", style= {'textAlign': 'center'}),
    dcc.Dropdown(
        id="market-type-dropdown",
        options=[{"label": mt, "value": mt} for mt in df["MARKET_TYPE"].unique()],
        value=df["MARKET_TYPE"].unique()[0],
        placeholder="Select a Market Type"
    ),
    dcc.Graph(id="map")
])

# Callback for interactivity
@app.callback(
    Output("map", "figure"),
    Input("market-type-dropdown", "value")
)
def update_map(selected_market_type):
    # Filter data based on selected market type
    filtered_data = df[df["MARKET_TYPE"] == selected_market_type]
    
    # Create map
    fig = px.scatter_geo(
        filtered_data,
        locations="ISO3",
        color="PROJECT_SCOPE",
        size="COUNT",
        hover_name="COUNTRY",
        projection="natural earth",
        title=f"Projects in {selected_market_type} Market",
        labels={"COUNT": "Project Count"}
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

{
  "editor.tokenColorCustomizations": {
    "textMateRules": [
      {
        "scope": "markup.heading",
        "settings": {
          "foreground": "#ff0000",
          "fontStyle": "bold"
        }
      }
    ]
  }
}
