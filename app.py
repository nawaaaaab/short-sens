from dash import Dash, dcc, html, Input, Output

neg_list = ['no', 'not', 'worst', "ohh"]
pos_list = ['yes', 'awesome', 'amazing']

app = Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1("Short Sentiment Analyzer Playground"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    if set(input_value.strip().split()).intersection(pos_list):
        result = 'Positive'
    else:
        result = 'Negative'
    
    return f'Output: {result}'


if __name__ == '__main__':
    app.run_server(debug=True)
