
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('D:/ankita/python/carbon-market/2025_0103_1434.csv', sep='\t', encoding='utf-8')

# Ensure 'COUNT' column exists for the size parameter
if 'COUNT' not in df.columns:
    df['COUNT'] = 1  # Assuming each row represents a single project

# Initialize Dash app
app = dash.Dash(__name__)

# Custom color scale
colorscale = px.colors.sequential.Plasma

# Layout with improved styling
app.layout = html.Div([
    html.Div([
        html.H1("Carbon Market Visualization", style={'textAlign': 'center', 'marginBottom': '10px'}),
        html.H3("Distribution of Carbon Credits by Project Scope", 
                style={'textAlign': 'center', 'marginBottom': '30px', 'color': '#666'})
    ]),
    
    html.Div([
        dcc.Dropdown(
            id="project-scope-dropdown",
            options=[{"label": mt, "value": mt} for mt in df["PROJECT_SCOPE"].unique()],
            value=df["PROJECT_SCOPE"].unique()[0],
            placeholder="Select a Project Scope",
            style={'width': '60%', 'margin': '0 auto'}
        )
    ], style={'padding': '20px 0'}),
    
    dcc.Graph(
        id="map",
        style={'height': '700px', 'margin': '0 20px'}
    )
])

# Callback for interactivity
@app.callback(
    Output("map", "figure"),
    Input("project-scope-dropdown", "value")
)
def update_map(selected_project_scope):
    # Filter and aggregate data
    filtered_data = df[df["PROJECT_SCOPE"] == selected_project_scope]
    aggregated_data = filtered_data.groupby(['COUNTRY', 'ISO3']).agg({
        'TOTAL_CREDITS_ISSUED': 'sum',
        'COUNT': 'sum'
    }).reset_index()

    # Find the country with maximum credits
    max_credits = aggregated_data['TOTAL_CREDITS_ISSUED'].max()
    max_country = aggregated_data[aggregated_data['TOTAL_CREDITS_ISSUED'] == max_credits]

    # Create choropleth map
    fig = px.choropleth(
        aggregated_data,
        locations="ISO3",
        color="TOTAL_CREDITS_ISSUED",
        hover_name="COUNTRY",
        custom_data=['COUNT'],
        color_continuous_scale=colorscale,
        projection="natural earth",
        labels={'TOTAL_CREDITS_ISSUED': 'Credits Issued'},
        range_color=[aggregated_data['TOTAL_CREDITS_ISSUED'].min(), 
                     aggregated_data['TOTAL_CREDITS_ISSUED'].max()]
    )
    
    # Add annotation for the country with maximum credits
    if not max_country.empty and max_credits > 0:
        fig.add_annotation(
            x=0.95,
            y=0.95,
            xref="paper",
            yref="paper",
            text=f"Highest Credits Issued: {max_country['COUNTRY'].values[0]}<br>({max_credits:,.0f})",
            showarrow=False,
            bgcolor="white",
            bordercolor="black",
            borderwidth=3,
            font=dict(size=14, color="red")
        )

    # update layout
    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        coloraxis_colorbar={
            'title': 'Total Credits Issued',
            'thickness': 20,
            'len': 0.75,
            'xanchor': 'left',
            'yanchor': 'middle'
        },
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='natural earth'
        ),
        title={
            'text': f"Project Scope: {selected_project_scope}",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 18}
        }
    )
    
    # Customize hover information
    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br><br>" +
                      "Total Credits Issued: %{z:,.0f}<br>" +
                      "Number of Projects: %{customdata[0]:,}<extra></extra>"
    )
    
    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)