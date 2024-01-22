import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ta.momentum import rsi

asset= "GGAL"
start_date = "2023-01-01"
end_date="2022-01-01"

data = yf.download(asset, start=start_date, end=None)

data["RSI"]=rsi(data["Close"],14,False)

fig = make_subplots(rows=2,cols=1,row_heights=[0.7,0.3],shared_xaxes=True,vertical_spacing=0.01)

fig.add_trace(go.Scatter(x=data.index, y=data["Close"]), row=1, col=1)
fig.add_trace(go.Scatter(x=data.index, y=data["RSI"]), row=2, col=1)

fig.add_trace(go.Scatter(x=data.index, y=[30]*len(data["RSI"]),name="RSI Señal de Compra",line=dict(color="green",width=1)), row=2, col=1)
fig.add_trace(go.Scatter(x=data.index, y=[70]*len(data["RSI"]),name="RSI Señal de Venta",line=dict(color="red",width=1)), row=2, col=1)

fig.update_yaxes(title_text="Precio GGAL",row=1,col=1)
fig.update_yaxes(title_text="RSI",row=2,col=1)

fig.update_layout(template="ggplot2")  # Para versiones más recientes de Plotly  #fig.update(template="ggplot2")

fig.show()