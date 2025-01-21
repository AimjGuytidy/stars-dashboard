import dash
import dash_html_components as html

#creating the app:
app = dash.Dash(__name__)

#creating app layout:
app.layout = html.Div([html.H1("Hello, World!",
                               style={
                                   "color": "blue",
                                   "fontSize": "40px",
                                   "marginLeft": "20%"
                               }),html.H1("checking what shows up")])

# run the app
if __name__ == "__main__":
    app.run_server(debug=True)
