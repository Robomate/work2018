import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        html.Button(id='add-button', children='Add', n_clicks=0),
        html.Button(id='del-button', children='Delete', n_clicks=0),
        html.Button(id='tog-button', children='Toggle', n_clicks=0),
        html.Div(id='clicked-button', children='del:0 add:0 tog:0 last:nan', style={'display': 'none'})
    ]),
    html.Div(id='display-clicked', children=""),
])

@app.callback(
    dash.dependencies.Output('display-clicked', 'children'),
    [dash.dependencies.Input('clicked-button', 'children')]

)
def button_action(clicked):

    last_clicked = clicked[-3:]

    if last_clicked == 'del':
        return "You clicked delete"
    if last_clicked == 'add':
        return "You clicked add"
    if last_clicked == 'tog':
        return "You clicked toggle"


@app.callback(
    dash.dependencies.Output('clicked-button', 'children'),
    [dash.dependencies.Input('del-button', 'n_clicks'),
     dash.dependencies.Input('add-button', 'n_clicks'),
     dash.dependencies.Input('tog-button', 'n_clicks')],
    [dash.dependencies.State('clicked-button', 'children')]
)
def updated_clicked(del_clicks, add_clicks, tog_clicks, prev_clicks):

    prev_clicks = dict([i.split(':') for i in prev_clicks.split(' ')])
    last_clicked = 'nan'

    if del_clicks > int(prev_clicks['del']):
        last_clicked = 'del'
    elif add_clicks > int(prev_clicks['add']):
        last_clicked = 'add'
    elif tog_clicks > int(prev_clicks['tog']):
        last_clicked = 'tog'

    cur_clicks = 'del:{} add:{} tog:{} last:{}'.format(del_clicks, add_clicks, tog_clicks, last_clicked)

    return cur_clicks

if __name__ == '__main__':
	app.run_server(debug=True, host='192.168.2.11',port= 9999)

