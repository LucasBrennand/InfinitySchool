import mysql.connector

class Create:
    def __init__(self):
        pass
    
    def create_menu(self):
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
            Create.create_menu()
            op = int(input("Escolha uma opção: "))
            match(op):
                case 1:
                    parametro_name = input("Digite um novo paramêtro SQL: ")
                    parametros.append(parametro_name)
                case 2:
                    parametros_join = ', '.join(parametros)
                    self.mycursor.execute(f"CREATE TABLE {table_name} ({parametros_join})")
                    self.mydb.commit()
                    print(f"Tabela '{table_name}' criada com sucesso!")
                    op = 0
                case 0:
                    print("Saindo...")
                case _:
                    print("Opção inválida")
