import mysql.connector

class Create:
    def __init__(self, db_connection, db_cursor):
        self.db_connection = db_connection
        self.db_cursor = db_cursor
    
    @staticmethod
    def create_menu():
        return """
          1 - Inserir um novo paramêtro
          2 - Finalizar e criar tabela
          0 - Sair
"""
    
    def create_table(self):
        table_name = input("Digite o nome da tabela: ")
        parametros = []
        op = ""

        while (op != 0):
            print(Create.create_menu())
            try:
                op = int(input("Escolha uma opção: "))
            except ValueError:
                print("Opção invalida")
                continue

            match(op):
                case 1:
                    parametro_name = input("Digite um novo paramêtro SQL: ")
                    parametros.append(parametro_name)
                    print(f"Paramêtros adicionados: {parametros}")
                case 2:
                    parametros_join = ', '.join(parametros)
                    self.db_cursor.execute(f"CREATE TABLE {table_name} ({parametros_join})")
                    self.db_connection.commit()
                    print(f"Tabela '{table_name}' criada com sucesso!")
                    op = 0
                case 0:
                    print("Saindo...")
                case _:
                    print("Opção inválida")
