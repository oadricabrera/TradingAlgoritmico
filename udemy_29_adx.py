import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ta.trend import ADXIndicator

asset= "GGAL"
start_date = "2023-01-01"
end_date="2022-01-01"

data = yf.download(asset, start=start_date, end=None)

adx=ADXIndicator(data["High"], data["Low"], data["Close"],14,False)

data["ADX"]=adx.adx()
data["MD+"]=adx.adx_pos()
data["MD-"]=adx.adx_neg()

fig = make_subplots(rows=2,cols=1,row_heights=[0.7,0.3],shared_xaxes=True,vertical_spacing=0.01)

fig.add_trace(go.Scatter(x=data.index, y=data["Close"],name="Precio de GGAL",line=dict(color="grey",width=1), fill="tonexty"),row=1,col=1)
fig.add_trace(go.Scatter(x=data.index, y=data["ADX"],name="ADX",line=dict(color="black",width=1)),row=2,col=1)

fig.add_trace(go.Scatter(x=data.index, y=data["MD+"],name="MD+",line=dict(color="green",width=1)),row=2,col=1)
fig.add_trace(go.Scatter(x=data.index, y=data["MD-"],name="MD-",line=dict(color="red",width=1)),row=2,col=1)

fig.update_yaxes(title_text="Precio GGAL",row=1,col=1)
fig.update_yaxes(title_text="ADX",row=2,col=1)

fig.show()