class Update:
    def __init__(self, db_connection, db_cursor):
        self.db_connection = db_connection
        self.db_cursor = db_cursor

    @staticmethod
    def create_menu():
        return """
          1 - Inserir um parâmetro e o valor novo
          2 - Inserir a condição (WHERE)
          3 - Finalizar e atualizar as tabelas
          0 - Sair
"""

    def update(self):
        op = ""
        colunas = []
        where_valor = ""
        try:
            tabela_input = input("Digite de qual tabela você quer atualizar: ")
        except ValueError:
            print("Essa tabela não existe")

        while (op != 0):
            print(Update.create_menu())
            op = int(input("Digite uma opção: "))
            match(op):
                case 1:
                    update_valor = input("Digite uma coluna e seu valor novo (ex: Nome = 'Lucas'): ")
                    colunas.append(update_valor)
                    print(f"Coluna adicionado: {update_valor}")
                case 2:
                    where_valor = input("Digite a condição para o WHERE (ex: ID = 2): ")
                case 3:
                    colunas_join = ', '.join(colunas)
                    self.db_cursor.execute(f"UPDATE {tabela_input} SET {colunas_join} WHERE {where_valor}")
                    self.db_connection.commit()
                    pass
                case 0:
                    print("Saindo...")
                case _:
                    print("Opção inválida")


# "UPDATE CLIENTE SET NOME=`JOSE` WHERE ID_NOME=1"