import pymysql

class RobotUdemy:
    HOST = "localhost"
    USER = "root"
    PASSWORD = "1QuieroMysql"
    DB = "bearybulldb"

    def __init__(self):
        self.connexion = pymysql.connect(
            host=RobotUdemy.HOST,
            user=RobotUdemy.USER,
            password=RobotUdemy.PASSWORD,
            db=RobotUdemy.DB,
            charset="utf8",
        )

    def seleccionar(self, query, params=None):
        """
        @query:str -> consulta sql que se va a ejecutar
        @params=None:tuple | list -> valores de los parametros

        @return:
        tuple(tuple) -> registros de la consulta
        """
        data = 0
        try:
            with self.connexion.cursor() as cursor:
                if params is None:
                    cursor.execute(query)
                else:
                    cursor.execute(query, params)
                data = cursor.fetchall()
        except Exception as e:
            print(f"Error {str(e)}")
        finally:
            return data

    def grabar_data(self, simulacro=True, query=None, params=None, orden_campos=None):
        """
        [+] Esta método actualiza,elimina o inserta un registro en la bd

        @query=None:str -> consulta sql que se va a ejecutar
        @params=None:tuple | list -> valores de los parametros

        @return:
        int -> registros afectados
        """
        datos=None
        if orden_campos:
            datos = [params.get(campo) for campo in orden_campos]
        
        if simulacro:
            return datos
        try:
            cant_registro = 0
            with self.connexion.cursor() as cursor:
                if params is not None:
                    cant_registro = cursor.execute(query, datos)
                else:
                    cant_registro = cursor.execute(query)
                self.connexion.commit()
        except Exception as e:
            print(f"Error {str(e)}")
        finally:
            return cant_registro
        
conexion_robot_udemy = RobotUdemy()

conexion_robot_udemy.grabar_data(query="insert into nombre_tabla(fecha_cotizacion,precio_venta) values(%s,%s)", params=('2023-11-20', 1.090702772140503),simulacro=False)       #"insert into nombre_tabla(fecha,precio_venta) values(%s,%s)"      


