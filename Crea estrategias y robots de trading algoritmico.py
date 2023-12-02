import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# df = yf.download("GOOG", interval="1d", start="2023-11-01", end=None)

# df=yf.download("GOOG", period="10y", interval="1d")

# varios tickers

asset = ["EURUSD=x", "EURGBP=x", "AUDUSD=x"]

precio_de_cierre = {}

for ticker in asset:
    # precio_de_cierre[ticker] = yf.download(ticker, period="2y", interval="1d")[
    #     "Adj Close"
    # ]
    precio_de_cierre.update({ticker: yf.download(ticker, period="2y", interval="1d")})

    # precios_db[ticker] = yf.download(ticker, period="2y", interval="1d")

# print(precio_de_cierre)

# precio_de_cierre["EURUSD=x"].plot(figsize=(15,6))
# plt.show()

# cada ticker
# print(precio_de_cierre.get("EURUSD=x").head())
# guarda fecha y precio: funciona bien
for fecha, precio in zip(
    precio_de_cierre.get("EURUSD=x").index, precio_de_cierre.get("EURUSD=x")["Open"]
):
    # print(f"fecha {fecha} precio {precio}")
    print({"fecha": fecha, "precio": precio})    
"""
df = pd.DataFrame(data={"Columna1":[1,2,3],
                        "Columna2":[4,5,6],
                        "Columna3":[7,8,9]                     
                        },
                        index=[2018,2019,2020]
                        )

print(df["Columna1"])
print(df.iloc[2][2])
df["Columna Nueva"]=[100,200,300]
print(df)

#copia de dataframe

copiadf=df.copy()

print(f"Compia Df: {copiadf}")
"""