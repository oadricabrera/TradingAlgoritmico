import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd
import numpy as np

df=yf.download("AMZ",start="2023-10-01")

df["EMA12"]=df.close.ewm(span=12).mean()
df["EMA26"]=df.close.ewm(span=26).mean()
df["MACD"]=df.EMA12-df.EMA26
df["Senal"]=df.MACD.ewm(span=9).mean()

plt.subplot(2,1,1)
plt.plot(df.Senal, color="red")
plt.plot(df.MACD)

Buy, Sell = [],[]
for i in range(2,len(df)):
    if df.MACD.iloc[i] > df.Senal.iloc[i] and df.MACD.iloc[i-1] < df.Senal.iloc[i-1]:
        Buy.append(i)
    elif df.MACD.iloc[i] < df.Senal.iloc[i] and df.MACD.iloc[i-1] > df.Senal.iloc[i-1]:
        Sell.append(i)

print("Dates sales")
print(df.iloc[Sell].index, df.iloc[Sell].Close)