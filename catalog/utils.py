import datetime as dt
import pandas_datareader.data as web

def get_data_from_yahoo(ticker):
    start = dt.datetime(2000,1,1)
    df = web.DataReader(ticker, 'yahoo', start)
    return df