class Delete:
    def __init__(self, db_connection, db_cursor):
        self.db_connection = db_connection
        self.db_cursor = db_cursor

    @staticmethod
    def create_menu():
        return """
          1 - Inserir a condição (WHERE)
          2 - Finalizar e deletar as colunas
          0 - Sair
"""


    def delete(self):
        op = ""
        where_valor = ""
        try:
            tabela_input = input("Digite de qual tabela você quer deletar: ")
        except ValueError:
            print("Essa tabela não existe")

        while (op != 0):
            print(Delete.create_menu())
            op = int(input("Digite uma opção: "))
            match(op):
                case 1:
                    where_valor = input("Digite a condição para o WHERE (ex: ID = 2): ")
                case 2:
                    self.db_cursor.execute(f"DELETE FROM {tabela_input} WHERE {where_valor}")
                    self.db_connection.commit()
                case 0:
                    print("Saindo...")
                case _:
                    print("Opção inválida")