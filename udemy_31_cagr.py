import yfinance as yf

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

print(CAGR(data))

