import yfinance as yf
import pandas as pd
import pymysql
from dotenv import load_dotenv
from os import getenv
load_dotenv()

SELECCIONAR = """
SELECT * FROM yahoofinance
"""

INSERTAR = """
        INSERT INTO cotizaciones
        SET
            fecha_y_hora = %s,
            precio = %s,
            volumen = %s
    """ 

class YahooFinance:
    HOST = getenv("HOST")
    USER = getenv("USER")
    PASSWORD = getenv("PASSWORD")
    DB = getenv("DB")

    def __init__(self):
        self.connexion = pymysql.connect(
            host=YahooFinance.HOST,
            user=YahooFinance.USER,
            password=YahooFinance.PASSWORD,
            db=YahooFinance.DB,
            charset="utf8",
        )
        self.cursor=self.connexion.cursor()


    def get_stock_data(self,*,ticker, start_date, end_date, interval='1m'):
        # Descarga los datos del ticker especificado
        data = yf.download(ticker, start=start_date, end=end_date, interval=interval)    
        return data

    def guardar_data(self,cotizacion):
        for dato in cotizacion:
            self.cursor.execute(cotizacion,(dato.get("fecha_y_hora"),dato.get("precio"),dato.get("volumen")))
            self.connexion.commit()


if __name__ == "__main__":
    # Especifica el ticker, la fecha de inicio, la fecha de finalización y el intervalo
    ticker = 'GGAL'  # Cambia esto por el ticker que desees
    start_date = '2024-09-07'
    end_date = '2024-09-13'
    print(f"{start_date},{end_date}")
    # Llama a la función para obtener los datos
    conn = YahooFinance()
    stock_data = conn.get_stock_data(ticker=ticker,start_date=start_date,end_date=end_date)

    conn.guardar_data(stock_data)
    
    # Muestra los datos obtenidos
    print(stock_data)

#guardar en datetime
#orm para bases de datos