import re
from django.shortcuts import render
from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.models import WheelZoomTool, RangeTool, ColumnDataSource, Range1d, HoverTool, CDSView, BooleanFilter
from bokeh.layouts import column

import requests
from math import pi

import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import os
import time
import sqlite3


def index(request):
    return render(request, 'catalog/index.html')


def get_data_from_yahoo(ticker):
    start = dt.datetime(2000,1,1)
    df = web.DataReader(ticker, 'yahoo', start)
    return df

#We use get_data method from utils
def get_stock(request):
    if request.method == "GET":
        ticker = request.GET['ticker']
        print(ticker)
        return render(request, 'catalog/index.html', {'ticker':ticker})

        # df = get_data_from_yahoo()
        # # print(source)
        # df.columns = [i.lower() for i in df.columns]
        # source = ColumnDataSource(data=df)
        # hover = HoverTool(
        #     tooltips=[
        #         ('d', '@datetime{%H:%M}'),
        #         ('o', '@open{0}'),
        #         ('h', '@high{0}'),
        #         ('l', '@low{0}'),
        #         ('c', '@close{0}'),
        #         ('v', '@volume{0}'),
        #     ],
        #     formatters={
        #         '@datetime': 'datetime'
        #     },
        #     mode='mouse'
        # )
        # inc_b = source.data['close'] > source.data['open']
        # inc = CDSView(source=source, filters=[BooleanFilter(inc_b)])
        # dec_b = source.data['open'] > source.data['close']
        # dec = CDSView(source=source, filters=[BooleanFilter(dec_b)])
        # w = 60000

        # p = figure(x_axis_type="datetime", sizing_mode="stretch_width", height=400)
        # p.segment(source=source, x0='datetime', x1='datetime', y0='high', y1='low', color="black")
        # p.vbar(source=source, view=inc, x='datetime', width=w, top='open', bottom='close', fill_color="green", line_color="green")
        # p.vbar(source=source, view=dec, x='datetime', width=w, top='open', bottom='close', fill_color="red", line_color="red")
        # p.line(source=source, x='datetime', y='bband_up', line_width=1, alpha=0.8, legend_label='bband_up', color='green')
        # p.line(source=source, x='datetime', y='bband_mid', line_width=1, alpha=0.8, legend_label='bband_mid', color='blue')
        # p.line(source=source, x='datetime', y='bband_low', line_width=1, alpha=0.8, legend_label='bband_low', color='red')
        # p.add_tools(hover)

        # show(p)