import yfinance as yf
import pandas as pd
import pymysql

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

class yahoofinance:
    HOST = "localhost"
    USER = "root"
    PASSWORD = "1QuieroMysql"
    DB = "yahoofinance"

    def __init__(self):
        print("-----> ", yahoofinance.HOST, yahoofinance.USER)
        self.connexion = pymysql.connect(
            host=yahoofinance.HOST,
            user=yahoofinance.USER,
            password=yahoofinance.PASSWORD,
            db=yahoofinance.DB,
            charset="utf8",
        )
        self.cursor=self.connexion.cursor()


    def get_stock_data(self,ticker, start_date, end_date, interval='1m'):
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
    start_date = '2024-06-25'
    end_date = '2024-07-02'
    
    # Llama a la función para obtener los datos
    stock_data = yahoofinance.get_stock_data(ticker, start_date, end_date)

    yahoofinance.guardar_data(stock_data)
    
    # Muestra los datos obtenidos
    print(stock_data)

#guardar en datetime
#orm para bases de datos