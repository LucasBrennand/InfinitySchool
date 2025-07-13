import mysql.connector

class Select:
    def __init__(self, db_connection, db_cursor):
        self.db_connection = db_connection
        self.db_cursor = db_cursor

    @staticmethod
    def create_menu():
        return """
        1 - Adicionar coluna de uma tabela para exibir
        2 - Mostrar todas as colunas de uma tabela
        3 - Finalizar e mostrar colunas
        0 - Sair
"""
    def select(self):
        op = ""
        colunas = []
        try:
            tabela_input = input("Digite de qual tabela você quer exibir: ")
        except ValueError:
            print("Essa tabela não existe")
    
        while (op != 0):
            print(Select.create_menu())
            try:
                op = int(input("Escolha uma opção: "))
            except ValueError:
                print("Opção invalida")
                continue

            match (op):
                case 1:
                    from_input = input("Digite uma coluna para exibir")
                    colunas.append(from_input)
                    print(f"Colunas escolhidas: {colunas}")
                case 2:
                    colunas = ["*"]
                case 3:
                    if colunas == []:
                        print("Colunas vazias")
                    else:
                        print(f"Colunas escolhidas: {colunas}")
                        colunas_join = ', '.join(colunas)
                        self.db_cursor.execute(f"SELECT {colunas_join} FROM {tabela_input}")
                        results = self.db_cursor.fetchall()
                        print(results)
                        colunas = []
                case 0:
                    print("Saindo...")
                    op = 0
                case _:
                    print("Opção inválida")
        