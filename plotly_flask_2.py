from flask import Flask, render_template

import json
import plotly
import time 

import pandas as pd
import numpy as np

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
	rng = pd.date_range('1/1/2011', periods=7500, freq='H')
	ts = pd.Series(np.random.randn(len(rng)), index=rng)

	for i in range(10):
		a = np.arange(i)
		b = np.arange(i)
		print(a)	
		graphs = [
			dict(
				data=[
					dict(
						x= a,
						y= b,
						type='scatter'
					),
				],
				layout=dict(
					title='Motor velocity'
				)
			)
		]
		
		# Add "ids" to each of the graphs to pass up to the client
		# for templating
		ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
		
		# Convert the figures to JSON
		# PlotlyJSONEncoder appropriately converts pandas, datetime, etc
		# objects to their JSON equivalents
		graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
	
		time.sleep(0.5)
	
	return render_template('layouts/index.html',
						   ids=ids,
						   graphJSON=graphJSON)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
    
