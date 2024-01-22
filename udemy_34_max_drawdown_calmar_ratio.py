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

def MDD(DF):
    df=DF.copy()
    df["retorno_diario"]=df["Adj Close"].pct_change()
    df["retorno_acumulativo"]=(1+df["retorno_diario"]).cumprod()
    df["max_ret_acum"]=df["retorno_acumulativo"].cummax()
    df["drawdown"]=df["max_ret_acum"]-df["retorno_acumulativo"]
    df["drawdown_pct"]=df["drawdown"]/df["max_ret_acum"]
    mdd=df["drawdown_pct"].max()
    return mdd

def CAGR(DF):               #contiene intervalos diarios
    df = DF.copy()                                      #crea una copia
    df["retorno_diario"]=df["Adj Close"].pct_change()
    df["retorno_acumulado"]=(1+df["retorno_diario"]).cumprod() 
    "añadimos 1 que significa que empezamos con 1 dolar, cumprod(): Calcula el producto acumulativo. Si se quiere la suma acumulativa, entonces ser+ia cumsum()"
    numero_de_anios=len(df)/252
    CAGR=(df["retorno_acumulado"].iloc[-1])**(1/numero_de_anios)-1   #[-1] para retornar el último valor del dataframe
    return CAGR

def Calmar_Ratio(DF):
    df=DF.copy()
    calmar=CAGR(df)/MDD(df)
    return calmar

print(f"MDD: {MDD(data)}")

print(f"Calmar Ratio: {Calmar_Ratio(data)}")