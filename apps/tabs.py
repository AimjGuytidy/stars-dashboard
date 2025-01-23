import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input

# app instantiation
app = dash.Dash(__name__, external_stylesheets= [dbc.themes.MINTY])

# information on the activities
timeline = ["first year", "second year"]
short_description = {"first year":"The data collection activities spanned 10 districts while gathering data on 343 schools where 100 schools were in the\
                     control group while 243 schools were in the treatment group",
                     "second year":"489 schools were visited across 10 districts to conduct STARS data collection activities."}

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
                                        ],
                                    style = {"marginLeft" : "2%",
                                             "marginRight" : "2%"}) 
                                ]),
                       dbc.Row([dbc.Tabs([
                                    dbc.Tab([html.Ul([html.Li(["Number of Activities: 3"]),
                                                    html.Li(["Temporal Coverage: 2023-2024"]),
                                                    html.Li(["Last Updated: August 2, 2024"]), 
                                                    html.Li(["Source: ",html.A("STARS documentation",
                                                                                href="https://ipastorage.app.box.com/folder/170575516047?s=54ebq7bdudq022jmqg3xk13gju4p3f28",
                                                                                target="blank")])])], label = "Key Facts", style = {"marginLeft" : "2%"}),
                                    dbc.Tab([html.Ul([html.Br(),
                                                    html.Li(["Description: The STARS program in Rwanda, which ties teacher merit awards to classroom inputs and pupil \
                                                            learning outcomes, has improved learning outcomes and will be adapted to incorporate these metrics into \
                                                            teachers' imihigo (performance contracts). A three-year rollout plan, aligned with the National Strategy \
                                                            for Accelerated Foundational Learning, will pilot and scale the initiative, leveraging data infrastructure \
                                                            and regulatory frameworks for nationwide implementation."],
                                                            style={"marginRight" : "20%"}),
                                                    html.Li(["Duration: 2023-2027"])])],label = "Project Info", style = {"marginLeft" : "2%"})
])
])
])

# callback functions
@app.callback(Output(component_id = "output_dropdown",
                     component_property= "children"),
              Input(component_id = "id_dropdown",
                    component_property = "value"))

def activity_info(timeline):
    if timeline is None:
        return "STARS project is being implemented by Innovation for Poverty Actions in partnership with Georgetown University, MINEDUC, REB, and NESA"
    return [html.H3(timeline), f'For the  {timeline}, {short_description[timeline]}']

# run the app
if __name__ == "__main__":
    app.run_server(debug=True)
