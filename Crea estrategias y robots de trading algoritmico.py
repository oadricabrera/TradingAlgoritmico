import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#df = yf.download("GOOG", interval="1d", start="2023-11-01", end=None)

#df=yf.download("GOOG", period="10y", interval="1d")

#varios tickers

asset=["EURUSD=x","EURGBP=x","AUDUSD=x"]

precio_de_cierre=pd.DataFrame()
precios_db=dict()

for ticker in asset:
    precio_de_cierre[ticker]=yf.download(ticker,period="2y", interval="1d")["Adj Close"]
    precios_db[ticker]=yf.download(ticker,period="2y", interval="1d")["Open"]

#print(precio_de_cierre)

#precio_de_cierre["EURUSD=x"].plot(figsize=(15,6))
#plt.show()

print(precios_db)




