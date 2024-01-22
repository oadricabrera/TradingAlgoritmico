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

def CAGR(DF):               #contiene intervalos diarios
    df = DF.copy()                                      #crea una copia
    df["retorno_diario"]=df["Adj Close"].pct_change()
    df["retorno_acumulado"]=(1+df["retorno_diario"]).cumprod() 
    "añadimos 1 que significa que empezamos con 1 dolar, cumprod(): Calcula el producto acumulativo. Si se quiere la suma acumulativa, entonces ser+ia cumsum()"
    numero_de_anios=len(df)/252
    CAGR=(df["retorno_acumulado"].iloc[-1])**(1/numero_de_anios)-1   #[-1] para retornar el último valor del dataframe
    return CAGR

def Volatilidad(DF):
    df=DF.copy()
    df["retorno_diario"]=df["Adj Close"].pct_change()
    vol=df["retorno_diario"].std()*np.sqrt(252)
    return vol

def Sharpe(DF,riskfree_rate=0.022): #tasa libre de riesgo
    df=DF.copy()
    sharpe_ratio=(CAGR(DF)-riskfree_rate)/Volatilidad(df)
    return sharpe_ratio

def Sortino(DF,riskfree_rate=0.022):
    df=DF.copy()
    df["retorno_diario"]*df["Adj Close"].pct_change()
    neg_vol=df[df["retorno_diario"]<0]["retorno_diario"].std()*np.sqrt(252)
    sortino_ratio=(CAGR(df)-riskfree_rate)/neg_vol
    return sortino_ratio

data["retorno_diario"]=data["Adj Close"].pct_change()

data[data["retorno_diario"]<0]["retorno_diario"]

print(f"Sortino Ratio: {Sortino(data)}")

