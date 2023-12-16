import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

precio_de_cierre = yf.download("EURUSD=x", period='7d', interval='1m')["Adj Close"]

precio_de_cierre.plot(figsize=(15,6))

#precio_de_cierre["Time"] = pd.to_datetime(precio_de_cierre["Time"],dayfirst=True)

print(precio_de_cierre)

plt.show()