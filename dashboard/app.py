from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Initialize the App
app = Dash(__name__, external_stylesheets=['styles.css'])

data = "./data/Salesstore.csv"
df = pd.read_csv(data)

segment_customers = df.groupby('Customer_Segment')['Order_ID'].nunique().reset_index()
segment_customers = segment_customers.sort_values(by='Order_ID', ascending=False)
Global_Sales = df['Sales'].sum()
Avg_Profit = df['Profit'].mean()


# Creating the bar graph
fig = px.bar(segment_customers, x='Customer_Segment', y='Order_ID', color='Customer_Segment', barmode='stack',width=800, height=400)
fig.update_layout(
    plot_bgcolor='#222235',
    paper_bgcolor='#222235',
    font_color='#D4D8DA',
    margin = dict(l=25, r=25, t=25, b=25)
)

# Create the layout
app.layout = html.Div([
        html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('bourane.png'),
                     id='corona-image',
                     style={
                         "height": "60px",
                         "width": "auto",
                         "margin-bottom": "25px",
                     },
                     )
        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H3("Sales Analysis", style={"margin-bottom": "0px", 'color': 'white'}),
            ])
        ], className="one-half column", id="title"),

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    html.Div([
        # the global Cases div
        html.Div([
            html.H6(children='Global Sales',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{Global_Sales:,.2f}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),

], className="card_container three columns",
        ),

# the global deaths div
        html.Div([
            html.H6(children='Avrerage Profit',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{Avg_Profit:,.2f}",
                   style={
                       'textAlign': 'center',
                       'color': '#dd1e35',
                       'fontSize': 40}
                   ),

], className="card_container three columns",
        ),

# the Global Recovered div
        html.Div([
            html.H6(children='Global Sales',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"300000",
                   style={
                       'textAlign': 'center',
                       'color': 'green',
                       'fontSize': 40}
                   ),
], className="card_container three columns",
        ),

# the Global Active div
        html.Div([
            html.H6(children='Global Sales',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"15.555",
                   style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 40}
                   ),

    ], className="card_container three columns")

    ], className="row flex-display"),
]
)

# The entry app 
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)







