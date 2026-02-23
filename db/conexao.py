import mysql.connector

def CriarConexao():
        return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="consulta"
    )