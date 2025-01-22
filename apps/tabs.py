import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

# app instantiation
app = dash.Dash(__name__, external_stylesheets= [dbc.themes.MINTY])

# app layout
app.layout = html.Div([dbc.Row([dbc.Col([html.H1("Innovation for Poverty Actions Projects",
                               style={
                                   "color": "#155240",
                                   "fontSize": "40px"
                               })],lg = {"size":6,
                            "offset": 4},md = 12)]),
                       dbc.Row([dbc.Col([html.H2("Supporting Teachers' Achievement in Rwandan Schools (STARS)",
                                style={"color": "#49AC57",
                                       "fontSize": "25px"})],lg = {"size":8,
                            "offset": 2},xl = {"size":8,
                            "offset": 2},md = 12)]),
                       dbc.Row([html.Div([
                                    dcc.Dropdown(id = "id_dropdown",
                                                options = [{"label" : time,
                                                            "value": time}
                                                            for time in timeline]),
                                    html.Br(),
                                    html.Div(id = "output_dropdown")
                                        ])
                                ]),
                       dbc.Row([dbc.Tabs([
                                    dbc.Tab([html.Ul([html.Li(["Number of Activities: 3"]),
                                                    html.Li(["Temporal Coverage: 2023-2024"]),
                                                    html.Li(["Last Updated: August 2, 2024"]), 
                                                    html.Li(["Source: ",html.A("STARS documentation",
                                                                                href="https://ipastorage.app.box.com/folder/170575516047?s=54ebq7bdudq022jmqg3xk13gju4p3f28",
                                                                                target="blank")])])], label = "Key Facts"),
                                    dbc.Tab([html.Ul([html.Br(),
                                                    html.Li(["Description: The STARS program in Rwanda, which ties teacher merit awards to classroom inputs and pupil \
                                                            learning outcomes, has improved learning outcomes and will be adapted to incorporate these metrics into \
                                                            teachers' imihigo (performance contracts). A three-year rollout plan, aligned with the National Strategy \
                                                            for Accelerated Foundational Learning, will pilot and scale the initiative, leveraging data infrastructure \
                                                            and regulatory frameworks for nationwide implementation."],
                                                            style={"marginRight" : "20%"}),
                                                    html.Li(["Duration: 2023-2027"])])],label = "Project Info")
])])])

# run the app
if __name__ == "__main__":
    app.run_server(debug=True)
