import yfinance as yf

# import pandas as pd
# import matplotlib.pyplot as plt
from conexion_robot_udemy import RobotUdemy, INSERT

df = yf.download("GOOG", interval="1d", start="2022-01-20", end=None)

# print(df)

# df=yf.download("GOOG", period="10y", interval="1d")

# varios tickers

asset = ["EURUSD=x", "EURGBP=x", "AUDUSD=x"]

precio_de_cierre = {}

for ticker in asset:
    # precio_de_cierre[ticker] = yf.download(ticker, period="2y", interval="1d")[
    #     "Adj Close"
    # ]
    precio_de_cierre.update({ticker: yf.download(ticker, period="1y", interval="1d")})

    # precios_db[ticker] = yf.download(ticker, period="2y", interval="1d")

# print(precio_de_cierre)

# precio_de_cierre["EURUSD=x"].plot(figsize=(15,6))
# plt.show()

# cada ticker
# print(precio_de_cierre.get("EURUSD=x").head())
# guarda fecha y precio: funciona bien
conexion_robot_udemy = RobotUdemy()
fecha, precio = (
    precio_de_cierre.get("EURUSD=x").index[-1],
    precio_de_cierre.get("EURUSD=x")["Adj Close"].iloc[-1],
)
conexion_robot_udemy.insertar_record(
    query=INSERT,
    data=(fecha, precio),
)

conexion_robot_udemy("SELECT fecha_cotizacion WHERE index[-1]")

if conexion_robot_udemy.fecha_cotizacion == fecha:
    print("La BD está actualizada")

print(f"{conexion_robot_udemy.fecha_cotizacion},{fecha},{precio}")
"""
for fecha, precio in zip(
    precio_de_cierre.get("EURUSD=x").index, precio_de_cierre.get("EURUSD=x")["Open"]
):
    # print(f"fecha {fecha} precio {precio}")
    print({"fecha": fecha, "precio": precio}) 
    conexion_robot_udemy.insertar_record(
        query=INSERT,
        data=(fecha, precio),
    )   

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


conexion = RobotUdemy()
#print(f"Igresando al for para guardar {len(BullSpreaddDB)} registros Bulls")
cantidad_registros = 1
cant_insert = 0
cant_insert += conexion.insertar_record(
        query=INSERT,
        data=("2023-11-20", 1.090702772140503),
    )

    
conexion.grabar_data(query="insert into nombre_tabla(fecha_cotizacion,precio_venta) values(%s,%s)", params=[{'fecha_cotizacion':'2023-11-20 00:00:00', 'precio_venta': 1.090702772140503}])       #"insert into nombre_tabla(fecha,precio_venta) values(%s,%s)"      

    if ((dato.get("precio_comprada_armado") != 0.0 and dato.get("precio_vendida_armado") != 0.0) or (dato.get("precio_comprada_desarme") != 0.0 and  dato.get("precio_vendida_desarme") != 0.0)):
        armada  = conexion.seleccionar(query=SELECCIONAR_GANANCIA_ARMADA,params=(dato.get("comprada"),dato.get("lanzada"))) #Me dice si el registro está en la BD
        desarme  = conexion.seleccionar(query=SELECCIONAR_GANANCIA_DESARME,params=(dato.get("comprada"),dato.get("lanzada")))
        if not armada:            
            #print(dato.get("ganancia_por_ciento_armada"),dato.get("ganancia_por_ciento_desarme"))
            conexion.grabar_data(simulacro=False,query=INSERTAR, params=dato) #daría un error, mis parámetros están en rows línea 82
        else:            
            # acá actualizas el registro con los valores que obtenes de la lista de dict
            id,armada = armada[0]
            id,desarme = desarme[0]
            #_id,_ganancia_por_ciento_armada,_ganancia_por_ciento_desarme=registros[0]
            data = get_data_armada(dato)
            if armada >= dato.get("ganancia_por_ciento_armada"):  #_ganancia_por_ciento_armada >= _data.get("ganancia_por_ciento_armada"):
                conexion.grabar_data(query=ACTUALIZAR_ESTRATEGIA_ARMADA, params=dato) #Puede funcionar, si hay error es por falta de datos
            data = get_data_desarme(dato)
            data.append(id)
            if desarme <= dato.get("ganancia_por_ciento_desarme"):
                conexion.grabar_data(query=ACTUALIZAR_ESTRATEGIA_DESARME, params=dato) #Puede funcionar, si hay error es por falta de datos
                            
#print(f"Igresando al for para guardar {len(BearSpreadDB)} registros Bears")
cantidad_registros = 
"""
