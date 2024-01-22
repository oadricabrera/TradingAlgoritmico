import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
from ta.trend import SMAIndicator
from ta.trend import EMAIndicator

asset= "GGAL"
start_date = "2023-01-01"
end_date="2022-01-01"

data = yf.download(asset, start=start_date, end=None)

sma4 = SMAIndicator(data["Close"],4,False)
sma12 = SMAIndicator(data["Close"],12,False)

data["SMA-4"]=sma4.sma_indicator()
data["SMA-12"]=sma12.sma_indicator()

fig = go.Figure()

fig.add_trace(go.Scatter(x=data.index, y=data["Close"], line=dict(color="grey"), name="Precio de Cierre"))
fig.add_trace(go.Scatter(x=data.index, y=data["SMA-4"], line=dict(color="cyan", width=1), name="SMA4"))
fig.add_trace(go.Scatter(x=data.index, y=data["SMA-12"], line=dict(color="blue", width=1), name="SMA12"))

fig.show()

data["EMA-20"]=EMAIndicator(data["Close"],20,False).ema_indicator()
data["EMA-150"]=EMAIndicator(data["Close"],150,False).ema_indicator()

fig.add_trace(go.Scatter(x=data.index, y=data["Close"], line=dict(color="grey"), name="Precio de Cierre"))
fig.add_trace(go.Scatter(x=data.index, y=data["EMA-20"], line=dict(color="cyan", width=1), name="EMA 20"))
fig.add_trace(go.Scatter(x=data.index, y=data["EMA-150"], line=dict(color="blue", width=1), name="EMA 150"))

fig.show()

print(data)
