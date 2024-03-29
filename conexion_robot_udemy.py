import pymysql
from querys_sql import INSERT


class RobotUdemy:
    HOST = "localhost"
    USER = "root"
    PASSWORD = "1QuieroMysql"
    DB = "robot_udemy"

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

    # def grabar_data(self, simulacro=True, query=None, params=None, orden_campos=None):
    #     """
    #     [+] Esta método actualiza,elimina o inserta un registro en la bd

    #     @query=None:str -> consulta sql que se va a ejecutar
    #     @params=None:tuple | list -> valores de los parametros

    #     @return:
    #     int -> registros afectados
    #     """
    #     datos=None
    #     if orden_campos:
    #         datos = [params.get(campo) for campo in orden_campos]

    #     if simulacro:
    #         return datos
    #     try:
    #         cant_registro = 0
    #         with self.connexion.cursor() as cursor:
    #             if params is not None:
    #                 cant_registro = cursor.execute(query, datos)
    #             else:
    #                 cant_registro = cursor.execute(query)
    #             self.connexion.commit()
    #     except Exception as e:
    #         print(f"Error {str(e)}")
    #     finally:
    #         return cant_registro

    def insertar_record(self, query=None, data=None):
        return self.grabar_data(query, data)

    def actualizar_record(self, query=None, data=None):
        return self.grabar_data(query, data)

    def eliminar_record(self, query=None, data=None):
        return self.grabar_data(query, data)

    def grabar_data(self, query=None, data=None):
        """
        [+] Esta método actualiza,elimina o inserta un registro en la bd

        @query=None:str -> consulta sql que se va a ejecutar
        @params=None:tuple | list -> valores de los parametros

        @return:
        int -> registros afectados
        """
        cant_registro = 0
        try:
            with self.connexion.cursor() as cursor:
                cant_registro = (
                    cursor.execute(query, data) if data else cursor.execute(query)
                )
                self.connexion.commit()
        except Exception as e:
            print(f"Error {str(e)}")
        finally:
            return cant_registro

"""
conexion_robot_udemy = RobotUdemy()
cant_insert = 0
for i in range(10):
    cant_insert += conexion_robot_udemy.insertar_record(
        query=INSERT,
        data=("2023-11-20", 1.090702772140503),
    )

print(f"Registros insertados {cant_insert}")
"""
