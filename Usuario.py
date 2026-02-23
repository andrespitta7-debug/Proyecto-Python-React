
from Conexion import *

class CAsunto:

    def mostrarAsunto():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado


        except mysql.connector.Error as error:
            print("Error de mostrar de datos {}".format(error))

    def ingresarAsunto(asunto,comentario):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql ="insert into usuarios values(null,%s,%s);"
            #La variable valores tiene que ser una tupla
            #Como mínima expresión es: (valor,) la coma hace que sea una tupla
            #Las tuplas son listas inmutables, eso quiere decir que no se pueden modificar
            valores = (asunto,comentario)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
        

    def editarAsunto(id,asunto,comentario):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql ="UPDATE usuarios SET usuarios.asunto=%s,usuarios.comentario=%s Where usuarios.id=%s;"
            valores = (asunto,comentario,id)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro actualizado")
            cone.close    

        
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
    
    def eliminarAsunto(id):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql ="DELETE from usuarios WHERE usuarios.id=%s;"
            valores = (id,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro eliminado")
            cone.close    

        
        except mysql.connector.Error as error:
            print("Error de eliminación de datos {}".format(error))
        