import mysql.connector
from create import Create
from selectsql import Select
from updatesql import Update
from deletesql import Delete
from dropsql import Drop

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

def menu():
    return """
1 - Criar uma nova tabela
2 - Selecionar colunas de uma tabela
3 - Atualizar colunas de uma tabela
4 - Deletar colunas de uma tabela
5 - Deletar uma tabela
0 - Sair 
"""

# CRUD
op = ""
while (op != 0):
    print(menu())
    op = int(input("Digite uma opção: "))
    print("*--------------------------------------------*")
    match (op):
        case 1:
            create = Create(mydb, mycursor)
            create.create_table()
        case 2:
            select = Select(mydb, mycursor)
            select.select()
        case 3:
            update = Update(mydb, mycursor)
            update.update()
        case 4:
            delete = Delete(mydb, mycursor)
            delete.delete()
        case 5:
            drop = Drop(mydb, mycursor)
            drop.drop()
        case 0:
            print("Fechando a conexão...")
            op = 0
        case _:
            print("Opção inválida")


if mydb.is_connected():
    mycursor.close()
    mydb.close()
    print("Conexão com o banco de dados fechada.")
                    
