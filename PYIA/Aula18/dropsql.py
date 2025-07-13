class Drop:
    def __init__(self, db_connection, db_cursor):
        self.db_connection = db_connection
        self.db_cursor = db_cursor

    @staticmethod
    def create_menu():
        return """
          1 - Deletar uma tabela
          0 - Sair
"""


    def drop(self):
        op = ""

        while (op != 0):
            print(Drop.create_menu())
            op = int(input("Digite uma opção: "))
            match (op):
                case 1:
                    tabela_input = input("Digite o nome da tabela: ")
                    drop_input = input("Tem certeza que você quer dar um DROP nessa tabela? Digite S/N: ")
                    if (drop_input.lower() == 's'):
                        self.db_cursor.execute(f"DROP TABLE {tabela_input}")
                        self.db_connection.commit()
                        print(f"Tabela {tabela_input} deletado com sucesso!")
                    elif (drop_input.lower() == 'n'):
                        print("Drop cancelado")
                    else:
                        print("Opção inválida..")
                case 0:
                    print("Saindo...")
                case _:
                    print("Opção inválida")
