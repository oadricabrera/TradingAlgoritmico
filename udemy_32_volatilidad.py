import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
from ta.volatility import AverageTrueRange
from ta.volatility import BollingerBands
from plotly.subplots import make_subplots
import numpy as np

asset= "GGAL"
start_date = "2023-01-01"
end_date="2022-01-01"

data = yf.download(asset, start=start_date, end=None)

data["Adj Close"].plot()

def volatilidad(DF):
    df=DF.copy()
    df["retorno_diario"]=df["Adj Close"].pct_change()
    vol=df["retorno_diario"].std()*np.sqrt(252)
    return vol

print(volatilidad(data))

