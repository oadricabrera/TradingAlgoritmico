import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
import matplotlib.pyplot as plt
from ta.trend import SMAIndicator
from ta.trend import EMAIndicator

asset= "GGAL"
start_date = "2023-01-01"
end_date="2022-01-01"

data = yf.download(asset, start=start_date, end=None)

sma_short = SMAIndicator(data["Adj Close"],50,False)
sma_long = SMAIndicator(data["Adj Close"],200,False)

data["sma_short"]=sma_short.sma_indicator()
data["sma_long"]=sma_long.sma_indicator()

data[["Adj Close","sma_short","sma_long"]].plot(figsize=(12,5),title="GGAL -SMA short(50) | SMA Long (200)", fontsize=12,secondary_y="posicion")
plt.legend(fontsize=12)
plt.show()

data.loc["2021"][["Adj Close","sma_short","sma_long"]].plot(figsize=(12,5),title="GGAL -SMA short(50) | SMA Long (200)", fontsize=12,secondary_y="posicion")
plt.legend(fontsize=12)
plt.show()

print(data)