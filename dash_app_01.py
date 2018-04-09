import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as dhc
import plotly
import random
import plotly.graph_objs as go
from collections import deque

ani = True # enable animation
# layouts
text_style_1 = dict(color='#444', textAlign = 'left', fontFamily='sans-serif', fontWeight=300) 
text_style_2 = dict(color='#444', textAlign = 'center', fontFamily='sans-serif', fontWeight=300) 

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)


app = dash.Dash(__name__)

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

# app layout
app.layout = dhc.Div(
    [   
        dhc.H2('Motor App', style=text_style_1),
        dhc.P('Monitor the Motor Velocity', style=text_style_2),
        dcc.Graph(id='live-graph', 
                  animate=ani
                  ),
        dcc.Interval(
            id='graph-update',
            interval= 1000 * 1
        ),
        dcc.Input(id='text1', placeholder='box', value=''),
        dhc.Button('Power On', id='button'),
        dcc.Markdown(children=markdown_text)
    ]
)

@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter():
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}



if __name__ == '__main__':
    app.run_server(debug=True, host='192.168.2.11',port= 9999)

