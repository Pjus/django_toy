import re
import numpy as np

from django.shortcuts import render
from .utils import get_data_from_yahoo

from bokeh.layouts import gridplot, column
from bokeh.plotting import figure, show
from bokeh.embed import components


p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'


from .utils import get_data_from_yahoo

def datetime(x):
    return np.array(x, dtype=np.datetime64)


#We use get_data method from utils
def get_stock(request):
    if request.method == "GET":
        ticker = request.GET['ticker']

        df = get_data_from_yahoo(ticker)
        df.columns = [i.lower() for i in df.columns]
        df['date'] = df.index

        print(df.head())

        p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
        p1.grid.grid_line_alpha=0.3
        p1.xaxis.axis_label = 'Date'
        p1.yaxis.axis_label = 'Price'

        p1.line(datetime(df['date']), df['adj close'], color='#A6CEE3', legend_label=ticker)
        p1.legend.location = "top_left"

        aapl = np.array(df['adj close'])
        aapl_dates = np.array(df['date'], dtype=np.datetime64)

        window_size = 30
        window = np.ones(window_size)/float(window_size)
        aapl_avg = np.convolve(aapl, window, 'same')

        p2 = figure(x_axis_type="datetime", title="AAPL One-Month Average")
        p2.grid.grid_line_alpha = 0
        p2.xaxis.axis_label = 'Date'
        p2.yaxis.axis_label = 'Price'
        p2.ygrid.band_fill_color = "olive"
        p2.ygrid.band_fill_alpha = 0.1

        p2.scatter(aapl_dates, aapl, size=4, legend_label='close',
                color='darkgrey', alpha=0.2)

        p2.line(aapl_dates, aapl_avg, legend_label='avg', color='navy')
        p2.legend.location = "top_left"

        script, div = components(column(p1, p2))

        return render(request, 'chart/graph.html', {'ticker':ticker, 'script':script, 'div':div})
