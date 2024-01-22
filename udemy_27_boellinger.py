import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
from ta.volatility import AverageTrueRange
from ta.volatility import BollingerBands
from plotly.subplots import make_subplots

asset= "GGAL"
start_date = "2023-01-01"
end_date="2022-01-01"

data = yf.download(asset, start=start_date, end=None)

atr=AverageTrueRange(data["High"], data["Low"], data["Close"],20,False)

data["ATR"]=atr.average_true_range()

print (data)

fig = make_subplots(rows=2,cols=1,row_heights=[0.6,0.4],shared_xaxes=True,vertical_spacing=0.01)

fig.add_trace(go.Scatter(x=data.index, y=data["Close"]), row=1, col=1)
fig.add_trace(go.Scatter(x=data.index, y=data["ATR"]), row=2, col=1)

fig.update_yaxes(title_text="Precio de GGAL",row=1,col=1)
fig.update_yaxes(title_text="ATR",row=2,col=1)

bandas_boellinger = BollingerBands(data["Close"],20,2,False)

data["BB-B. Alta"]=bandas_boellinger.bollinger_hband()
data["BB-B. Baja"]=bandas_boellinger.bollinger_lband()
data["BB-B. Media"]=bandas_boellinger.bollinger_mavg()
data["BB-Altura"]=bandas_boellinger.bollinger_wband()

fig = make_subplots(rows=2,cols=1,row_heights=[0.7,0.3],shared_xaxes=True,vertical_spacing=0.01)

fig.add_trace(go.Scatter(x=data.index, y=data["Close"]), row=1, col=1)
fig.add_trace(go.Scatter(x=data.index, y=data["BB-B. Alta"],line=dict(color="grey",width=1)), row=1, col=1)
fig.add_trace(go.Scatter(x=data.index, y=data["BB-B. Baja"],line=dict(color="grey",width=1),fill="tonexty"), row=1, col=1)
fig.add_trace(go.Scatter(x=data.index, y=data["BB-B. Media"]), row=2, col=1)

fig.add_trace(go.Scatter(x=data.index, y=data["ATR"],name="ATR"), row=2, col=1)

fig.update_yaxes(title_text="Precio GGAL",row=1,col=1)

fig.show()