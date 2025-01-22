import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

#creating the app:
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.MINTY])

#creating app layout:
app.layout = html.Div([html.H1("Innovation for Poverty Actions Projects",
                               style={
                                   "color": "#155240",
                                   "fontSize": "40px",
                                   "marginLeft": "20%"
                               }),
                        html.H2("Supporting Teachers' Achievement in Rwandan Schools (STARS)",
                                style={"color": "#49AC57",
                                       "fontSize": "25px"}),
                        html.P(["Key Facts:"]),
                        html.Ul([html.Li(["Number of Activities: 3"]),html.Li(["Temporal Coverage: 2023-2024"]),
                                 html.Li(["Last Updated: August 2, 2024"]), html.Li(["Source: ",html.A("STARS documentation",
                                                                                            href="https://ipastorage.app.box.com/folder/170575516047?s=54ebq7bdudq022jmqg3xk13gju4p3f28",
                                                                                            target="blank")])])])

# run the app
if __name__ == "__main__":
    app.run_server(debug=True)
