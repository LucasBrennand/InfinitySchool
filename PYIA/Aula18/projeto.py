import mysql.connector
from create import Create

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crud"
    )
    mycursor = mydb.cursor()
    print("Conexão com o banco de dados estabelecida com sucesso!")
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao banco de dados: {err}")
    exit()


create = Create()
create.create_table()

if mydb.is_connected():
    mycursor.close()
    mydb.close()
    print("Conexão com o banco de dados fechada.")
                    
