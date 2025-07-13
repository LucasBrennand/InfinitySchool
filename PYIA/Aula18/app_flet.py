import flet as ft
import mysql.connector
from flet import Colors # Explicitly import Colors

# Variáveis globais para a conexão com o banco de dados
# Serão inicializadas na função main do Flet
db_connection = None
db_cursor = None

def main(page: ft.Page):
    # Configurações básicas da página Flet
    page.title = "CRUD MySQL Flet App"
    page.vertical_alignment = ft.CrossAxisAlignment.START # Alinhamento vertical do conteúdo
    page.window_width = 800
    page.window_height = 600
    page.scroll = ft.ScrollMode.AUTO # Habilita rolagem se o conteúdo exceder a altura da janela

    # Elementos da UI para mensagens de status e entrada principal
    status_text = ft.Text(value="Conectando ao banco de dados...", size=16, weight=ft.FontWeight.BOLD)
    main_input_field = ft.TextField(label="Digite uma opção", width=300, on_submit=lambda e: handle_main_menu_selection(e.control.value))
    output_area = ft.Column() # Área para exibir saída dinâmica das operações

    # --- Lógica de Conexão com o Banco de Dados ---
    def connect_db():
        """Tenta estabelecer a conexão com o banco de dados MySQL."""
        global db_connection, db_cursor # Declara que estamos usando as variáveis globais
        try:
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="crud"
            )
            db_cursor = db_connection.cursor()
            status_text.value = "Conexão com o banco de dados estabelecida com sucesso!"
            status_text.color = Colors.GREEN_700 # Changed to Colors.GREEN_700
            page.update() # Atualiza a UI para mostrar a mensagem de sucesso
            return True
        except mysql.connector.Error as err:
            status_text.value = f"Erro ao conectar ao banco de dados: {err}"
            status_text.color = Colors.RED_700 # Changed to Colors.RED_700
            page.update() # Atualiza a UI para mostrar a mensagem de erro
            return False

    # Tenta conectar ao banco de dados ao iniciar o aplicativo
    if not connect_db():
        page.add(status_text) # Adiciona apenas a mensagem de erro se a conexão falhar
        return # Interrompe a execução se a conexão falhar

    # --- Menu Principal da UI ---
    def get_main_menu_text():
        """Retorna o texto do menu principal."""
        return """
1 - Criar uma nova tabela
2 - Selecionar colunas de uma tabela
3 - Atualizar colunas de uma tabela
4 - Deletar linhas de uma tabela
5 - Deletar uma tabela
0 - Sair 
"""

    main_menu_display = ft.Text(value=get_main_menu_text(), size=18, font_family="monospace")

    # --- Classes de Operação CRUD (Adaptadas para Flet) ---

    class Create:
        """Classe para criar novas tabelas no banco de dados."""
        def __init__(self, page_ref: ft.Page, db_conn, db_curs, output_col: ft.Column, on_finish_callback):
            self.page = page_ref # Referência à página Flet
            self.db_connection = db_conn
            self.db_cursor = db_curs
            self.output_area = output_col # Área de saída para esta operação
            self.on_finish = on_finish_callback # Callback para retornar ao menu principal
            
            # Campos de entrada para a UI de criação
            self.table_name_field = ft.TextField(label="Nome da Tabela", width=300)
            self.param_name_field = ft.TextField(label="Parâmetro SQL (ex: id INT PRIMARY KEY)", width=400)
            self.current_params = [] # Lista para armazenar os parâmetros da tabela

        @staticmethod
        def create_menu_text():
            """Retorna o texto do menu de criação de tabela."""
            return """
              1 - Inserir um novo parâmetro
              2 - Finalizar e criar tabela
              0 - Sair
"""

        def show_create_ui(self):
            """Exibe a interface do usuário para criar uma tabela."""
            self.output_area.controls.clear() # Limpa a área de saída
            self.output_area.controls.append(ft.Text("--- Criar Tabela ---", size=20, weight=ft.FontWeight.BOLD))
            self.output_area.controls.append(self.table_name_field)
            self.output_area.controls.append(ft.Text(self.create_menu_text(), size=16, font_family="monospace"))
            self.output_area.controls.append(self.param_name_field)

            def add_param(e):
                """Adiciona um parâmetro à lista de colunas da tabela."""
                param = self.param_name_field.value.strip()
                if param:
                    self.current_params.append(param)
                    self.output_area.controls.append(ft.Text(f"Parâmetro adicionado: '{param}'"))
                    self.param_name_field.value = "" # Limpa o campo de entrada
                else:
                    self.output_area.controls.append(ft.Text("Por favor, digite um parâmetro válido.", color=Colors.RED_500)) # Changed to Colors.RED_500
                self.page.update() # Atualiza a UI

            def finalize_create(e):
                """Finaliza a criação da tabela e executa a query SQL."""
                table_name = self.table_name_field.value.strip()
                if not table_name:
                    self.output_area.controls.append(ft.Text("Nome da tabela não pode ser vazio.", color=Colors.RED_500)) # Changed to Colors.RED_500
                    self.page.update()
                    return
                
                if not self.current_params:
                    self.output_area.controls.append(ft.Text("Nenhum parâmetro adicionado para criar a tabela.", color=Colors.RED_500)) # Changed to Colors.RED_500
                    self.page.update()
                    return

                params_join = ', '.join(self.current_params)
                sql_create_table = f"CREATE TABLE {table_name} ({params_join})"
                
                try:
                    self.db_cursor.execute(sql_create_table)
                    self.db_connection.commit() # Confirma as alterações no banco de dados
                    self.output_area.controls.append(ft.Text(f"Tabela '{table_name}' criada com sucesso!", color=Colors.GREEN_700)) # Changed to Colors.GREEN_700
                except mysql.connector.Error as err:
                    self.output_area.controls.append(ft.Text(f"Erro ao criar tabela: {err}", color=Colors.RED_700)) # Changed to Colors.RED_700
                
                self.page.update()
                self.on_finish() # Retorna ao menu principal após a operação

            def exit_create(e):
                """Sai da operação de criação de tabela."""
                self.output_area.controls.append(ft.Text("Saindo da criação de tabela.", color=Colors.AMBER_700)) # Changed to Colors.AMBER_700
                self.page.update()
                self.on_finish() # Retorna ao menu principal

            # Adiciona botões para as ações de criação
            self.output_area.controls.append(
                ft.Row([
                    ft.ElevatedButton("Adicionar Parâmetro (1)", on_click=add_param),
                    ft.ElevatedButton("Finalizar e Criar (2)", on_click=finalize_create),
                    ft.ElevatedButton("Sair (0)", on_click=exit_create)
                ])
            )
            self.page.update()

    class Select:
        """Classe para selecionar e exibir dados de tabelas."""
        def __init__(self, page_ref: ft.Page, db_conn, db_curs, output_col: ft.Column, on_finish_callback):
            self.page = page_ref
            self.db_connection = db_conn
            self.db_cursor = db_curs
            self.output_area = output_col
            self.on_finish = on_finish_callback
            
            # Campos de entrada para a UI de seleção
            self.table_name_field = ft.TextField(label="Nome da Tabela", width=300)
            self.column_name_field = ft.TextField(label="Coluna para exibir (deixe vazio para todas)", width=400)
            self.selected_columns = [] # Lista para armazenar as colunas selecionadas

        @staticmethod
        def create_menu_text():
            """Retorna o texto do menu de seleção."""
            return """
            1 - Adicionar coluna para exibir
            2 - Mostrar todas as colunas
            3 - Finalizar e mostrar colunas
            0 - Sair
"""

        def show_select_ui(self):
            """Exibe a interface do usuário para selecionar dados."""
            self.output_area.controls.clear()
            self.output_area.controls.append(ft.Text("--- Selecionar Dados ---", size=20, weight=ft.FontWeight.BOLD))
            self.output_area.controls.append(self.table_name_field)
            self.output_area.controls.append(ft.Text(self.create_menu_text(), size=16, font_family="monospace"))
            self.output_area.controls.append(self.column_name_field)

            def add_column(e):
                """Adiciona uma coluna à lista de colunas a serem exibidas."""
                col = self.column_name_field.value.strip()
                if col:
                    self.selected_columns.append(col)
                    self.output_area.controls.append(ft.Text(f"Coluna adicionada: '{col}'"))
                    self.column_name_field.value = ""
                else:
                    self.output_area.controls.append(ft.Text("Por favor, digite um nome de coluna.", color=Colors.RED_500)) # Changed to Colors.RED_500
                self.page.update()

            def select_all_columns(e):
                """Define para selecionar todas as colunas ('*')."""
                self.selected_columns = ["*"]
                self.output_area.controls.append(ft.Text("Todas as colunas selecionadas.", color=Colors.BLUE_700)) # Changed to Colors.BLUE_700
                self.page.update()

            def finalize_select(e):
                """Finaliza a seleção e executa a query SQL para exibir os dados."""
                table_name = self.table_name_field.value.strip()
                if not table_name:
                    self.output_area.controls.append(ft.Text("Nome da tabela não pode ser vazio.", color=Colors.RED_500)) # Changed to Colors.RED_500
                    self.page.update()
                    return
                
                if not self.selected_columns:
                    self.output_area.controls.append(ft.Text("Nenhuma coluna selecionada.", color=Colors.RED_500)) # Changed to Colors.RED_500
                    self.page.update()
                    return

                columns_join = ', '.join(self.selected_columns)
                sql_query = f"SELECT {columns_join} FROM {table_name}"
                
                try:
                    self.db_cursor.execute(sql_query)
                    results = self.db_cursor.fetchall() # Busca todos os resultados
                    
                    self.output_area.controls.append(ft.Text(f"\n--- Resultados para '{table_name}' ---", size=18, weight=ft.FontWeight.BOLD))
                    
                    # Exibe os nomes das colunas como cabeçalho
                    if self.db_cursor.description:
                        column_names = [i[0] for i in self.db_cursor.description]
                        self.output_area.controls.append(ft.Text(" | ".join(column_names), weight=ft.FontWeight.BOLD))
                        self.output_area.controls.append(ft.Text("-" * (len(" | ".join(column_names)) + 2)))

                    # Exibe as linhas de resultados
                    if results:
                        for row in results:
                            self.output_area.controls.append(ft.Text(" | ".join(map(str, row))))
                    else:
                        self.output_area.controls.append(ft.Text("Nenhum resultado encontrado.", color=Colors.AMBER_700)) # Changed to Colors.AMBER_700
                    
                except mysql.connector.Error as err:
                    self.output_area.controls.append(ft.Text(f"Erro ao executar a consulta: {err}", color=Colors.RED_700)) # Changed to Colors.RED_700
                
                self.page.update()
                self.on_finish() # Retorna ao menu principal

            def exit_select(e):
                """Sai da operação de seleção de dados."""
                self.output_area.controls.append(ft.Text("Saindo da seleção de dados.", color=Colors.AMBER_700)) # Changed to Colors.AMBER_700
                self.page.update()
                self.on_finish()

            # Adiciona botões para as ações de seleção
            self.output_area.controls.append(
                ft.Row([
                    ft.ElevatedButton("Adicionar Coluna (1)", on_click=add_column),
                    ft.ElevatedButton("Todas as Colunas (2)", on_click=select_all_columns),
                    ft.ElevatedButton("Finalizar e Mostrar (3)", on_click=finalize_select),
                    ft.ElevatedButton("Sair (0)", on_click=exit_select)
                ])
            )
            self.page.update()

    class Update:
        """Classe para atualizar dados em tabelas."""
        def __init__(self, page_ref: ft.Page, db_conn, db_curs, output_col: ft.Column, on_finish_callback):
            self.page = page_ref
            self.db_connection = db_conn
            self.db_cursor = db_curs
            self.output_area = output_col
            self.on_finish = on_finish_callback
            
            # Campos de entrada para a UI de atualização
            self.table_name_field = ft.TextField(label="Nome da Tabela", width=300)
            self.update_pair_field = ft.TextField(label="Coluna e novo valor (ex: Nome = 'Lucas')", width=400)
            self.where_condition_field = ft.TextField(label="Condição WHERE (ex: ID = 2)", width=400)
            self.update_pairs = [] # Lista para armazenar os pares coluna=valor
            self.where_clause = "" # Cláusula WHERE

        @staticmethod
        def create_menu_text():
            """Retorna o texto do menu de atualização."""
            return """
            1 - Inserir um parâmetro e o valor novo
            2 - Inserir a condição (WHERE)
            3 - Finalizar e atualizar
            0 - Sair
"""

        def show_update_ui(self):
            """Exibe a interface do usuário para atualizar dados."""
            self.output_area.controls.clear()
            self.output_area.controls.append(ft.Text("--- Atualizar Dados ---", size=20, weight=ft.FontWeight.BOLD))
            self.output_area.controls.append(self.table_name_field)
            self.output_area.controls.append(ft.Text(self.create_menu_text(), size=16, font_family="monospace"))
            self.output_area.controls.append(self.update_pair_field)
            self.output_area.controls.append(self.where_condition_field)

            def add_update_pair(e):
                """Adiciona um par coluna=valor para atualização."""
                pair = self.update_pair_field.value.strip()
                if pair:
                    self.update_pairs.append(pair)
                    self.output_area.controls.append(ft.Text(f"Parâmetro de atualização adicionado: '{pair}'"))
                    self.update_pair_field.value = ""
                else:
                    self.output_area.controls.append(ft.Text("Por favor, digite um par coluna/valor válido.", color=Colors.RED_500)) # Changed to Colors.RED_500
                self.page.update()

            def set_where_condition(e):
                """Define a condição WHERE para a atualização."""
                condition = self.where_condition_field.value.strip()
                if condition:
                    self.where_clause = condition
                    self.output_area.controls.append(ft.Text(f"Condição WHERE definida: '{condition}'"))
                else:
                    self.output_area.controls.append(ft.Text("Condição WHERE não pode ser vazia.", color=Colors.RED_500)) # Changed to Colors.RED_500
                self.page.update()

            def finalize_update(e):
                """Finaliza a atualização e executa a query SQL."""
                table_name = self.table_name_field.value.strip()
                if not table_name:
                    self.output_area.controls.append(ft.Text("Nome da tabela não pode ser vazio.", color=Colors.RED_500)) # Changed to Colors.RED_500
                    self.page.update()
                    return
                
                if not self.update_pairs:
                    self.output_area.controls.append(ft.Text("Nenhum parâmetro de atualização (SET) foi inserido.", color=Colors.RED_500)) # Changed to Colors.RED_500
                    self.page.update()
                    return

                set_clause_join = ', '.join(self.update_pairs)
                sql_update_query = f"UPDATE {table_name} SET {set_clause_join}"
                
                if self.where_clause:
                    sql_update_query += f" WHERE {self.where_clause}"
                else:
                    self.output_area.controls.append(ft.Text("AVISO: Nenhuma condição WHERE definida! Isso irá atualizar TODAS as linhas da tabela.", color=Colors.ORANGE_500)) # Changed to Colors.ORANGE_500
                    # Em uma aplicação real, você adicionaria uma caixa de diálogo de confirmação aqui.

                try:
                    self.db_cursor.execute(sql_update_query)
                    self.db_connection.commit() # Confirma as alterações
                    self.output_area.controls.append(ft.Text(f"Tabela '{table_name}' atualizada com sucesso! Linhas afetadas: {self.db_cursor.rowcount}", color=Colors.GREEN_700)) # Changed to Colors.GREEN_700
                except mysql.connector.Error as err:
                    self.output_area.controls.append(ft.Text(f"Erro ao atualizar tabela: {err}", color=Colors.RED_700)) # Changed to Colors.RED_700
                
                self.page.update()
                self.on_finish()

            def exit_update(e):
                """Sai da operação de atualização de dados."""
                self.output_area.controls.append(ft.Text("Saindo da atualização de dados.", color=Colors.AMBER_700)) # Changed to Colors.AMBER_700
                self.page.update()
                self.on_finish()

            # Adiciona botões para as ações de atualização
            self.output_area.controls.append(
                ft.Row([
                    ft.ElevatedButton("Adicionar Parâmetro (1)", on_click=add_update_pair),
                    ft.ElevatedButton("Definir Condição WHERE (2)", on_click=set_where_condition),
                    ft.ElevatedButton("Finalizar e Atualizar (3)", on_click=finalize_update),
                    ft.ElevatedButton("Sair (0)", on_click=exit_update)
                ])
            )
            self.page.update()

    class Delete:
        """Classe para deletar linhas de tabelas."""
        def __init__(self, page_ref: ft.Page, db_conn, db_curs, output_col: ft.Column, on_finish_callback):
            self.page = page_ref
            self.db_connection = db_conn
            self.db_cursor = db_curs
            self.output_area = output_col
            self.on_finish = on_finish_callback
            
            # Campos de entrada para a UI de exclusão
            self.table_name_field = ft.TextField(label="Nome da Tabela", width=300)
            self.where_condition_field = ft.TextField(label="Condição WHERE (ex: ID = 2)", width=400)
            self.where_clause = ""

        @staticmethod
        def create_menu_text():
            """Retorna o texto do menu de exclusão de linhas."""
            return """
            1 - Inserir a condição (WHERE)
            2 - Finalizar e deletar as linhas
            0 - Sair
"""

        def show_delete_ui(self):
            """Exibe a interface do usuário para deletar dados."""
            self.output_area.controls.clear()
            self.output_area.controls.append(ft.Text("--- Deletar Dados ---", size=20, weight=ft.FontWeight.BOLD))
            self.output_area.controls.append(self.table_name_field)
            self.output_area.controls.append(ft.Text(self.create_menu_text(), size=16, font_family="monospace"))
            self.output_area.controls.append(self.where_condition_field)

            def set_where_condition(e):
                """Define a condição WHERE para a exclusão."""
                condition = self.where_condition_field.value.strip()
                if condition:
                    self.where_clause = condition
                    self.output_area.controls.append(ft.Text(f"Condição WHERE definida: '{condition}'"))
                else:
                    self.output_area.controls.append(ft.Text("Condição WHERE não pode ser vazia.", color=Colors.RED_500)) # Changed to Colors.RED_500
                self.page.update()

            def finalize_delete(e):
                """Finaliza a exclusão e executa a query SQL."""
                table_name = self.table_name_field.value.strip()
                if not table_name:
                    self.output_area.controls.append(ft.Text("Nome da tabela não pode ser vazio.", color=Colors.RED_500)) # Changed to Colors.RED_500
                    self.page.update()
                    return
                
                if not self.where_clause:
                    self.output_area.controls.append(ft.Text("AVISO: Nenhuma condição WHERE definida! Isso irá deletar TODAS as linhas da tabela.", color=Colors.ORANGE_500)) # Changed to Colors.ORANGE_500
                    # Em uma aplicação real, você adicionaria uma caixa de diálogo de confirmação aqui.

                sql_delete_query = f"DELETE FROM {table_name}"
                if self.where_clause:
                    sql_delete_query += f" WHERE {self.where_clause}"

                try:
                    self.db_cursor.execute(sql_delete_query)
                    self.db_connection.commit() # Confirma as alterações
                    self.output_area.controls.append(ft.Text(f"Dados deletados com sucesso da tabela '{table_name}'! Linhas afetadas: {self.db_cursor.rowcount}", color=Colors.GREEN_700)) # Changed to Colors.GREEN_700
                except mysql.connector.Error as err:
                    self.output_area.controls.append(ft.Text(f"Erro ao deletar dados: {err}", color=Colors.RED_700)) # Changed to Colors.RED_700
                
                self.page.update()
                self.on_finish()

            def exit_delete(e):
                """Sai da operação de exclusão de dados."""
                self.output_area.controls.append(ft.Text("Saindo da exclusão de dados.", color=Colors.AMBER_700)) # Changed to Colors.AMBER_700
                self.page.update()
                self.on_finish()

            # Adiciona botões para as ações de exclusão
            self.output_area.controls.append(
                ft.Row([
                    ft.ElevatedButton("Definir Condição WHERE (1)", on_click=set_where_condition),
                    ft.ElevatedButton("Finalizar e Deletar (2)", on_click=finalize_delete),
                    ft.ElevatedButton("Sair (0)", on_click=exit_delete)
                ])
            )
            self.page.update()

    class Drop:
        """Classe para deletar tabelas inteiras."""
        def __init__(self, page_ref: ft.Page, db_conn, db_curs, output_col: ft.Column, on_finish_callback):
            self.page = page_ref
            self.db_connection = db_conn
            self.db_cursor = db_curs
            self.output_area = output_col
            self.on_finish = on_finish_callback
            
            # Campo de entrada para o nome da tabela a ser deletada
            self.table_name_field = ft.TextField(label="Nome da Tabela para Deletar", width=300)

        @staticmethod
        def create_menu_text():
            """Retorna o texto do menu de exclusão de tabela."""
            return """
            1 - Deletar uma tabela
            0 - Sair
"""

        def show_drop_ui(self):
            """Exibe a interface do usuário para deletar uma tabela."""
            self.output_area.controls.clear()
            self.output_area.controls.append(ft.Text("--- Deletar Tabela ---", size=20, weight=ft.FontWeight.BOLD))
            self.output_area.controls.append(ft.Text(self.create_menu_text(), size=16, font_family="monospace"))
            self.output_area.controls.append(self.table_name_field)

            def finalize_drop_confirmation(e):
                """Solicita confirmação antes de deletar a tabela."""
                table_name = self.table_name_field.value.strip()
                if not table_name:
                    self.output_area.controls.append(ft.Text("Nome da tabela não pode ser vazio.", color=Colors.RED_500)) # Changed to Colors.RED_500
                    self.page.update()
                    return
                
                # Limpa a área de saída e adiciona a mensagem de confirmação
                self.output_area.controls.clear()
                self.output_area.controls.append(ft.Text(f"Tem certeza que quer DELETAR a tabela '{table_name}'? Esta ação é irreversível.", color=Colors.ORANGE_700, size=16)) # Changed to Colors.ORANGE_700
                
                def confirm_action_buttons(e_btn):
                    """Executa a ação de DROP ou cancela com base na confirmação."""
                    if e_btn.control.text == "Sim":
                        sql_drop_query = f"DROP TABLE {table_name}"
                        try:
                            self.db_cursor.execute(sql_drop_query)
                            self.db_connection.commit()
                            self.output_area.controls.append(ft.Text(f"Tabela '{table_name}' deletada com sucesso!", color=Colors.GREEN_700)) # Changed to Colors.GREEN_700
                        except mysql.connector.Error as err:
                            self.output_area.controls.append(ft.Text(f"Erro ao deletar tabela: {err}", color=Colors.RED_700)) # Changed to Colors.RED_700
                    else:
                        self.output_area.controls.append(ft.Text("Operação de DROP cancelada.", color=Colors.AMBER_700)) # Changed to Colors.AMBER_700
                    
                    self.page.update()
                    self.on_finish() # Retorna ao menu principal após a confirmação/ação

                # Adiciona botões Sim/Não para a confirmação
                self.output_area.controls.append(
                    ft.Row([
                        ft.ElevatedButton("Sim", on_click=confirm_action_buttons),
                        ft.ElevatedButton("Não", on_click=confirm_action_buttons)
                    ])
                )
                self.page.update()

            def exit_drop(e):
                """Sai da operação de exclusão de tabela."""
                self.output_area.controls.append(ft.Text("Saindo da exclusão de tabela.", color=Colors.AMBER_700)) # Changed to Colors.AMBER_700
                self.page.update()
                self.on_finish()

            # Adiciona botões para as ações de DROP
            self.output_area.controls.append(
                ft.Row([
                    ft.ElevatedButton("Deletar Tabela (1)", on_click=finalize_drop_confirmation),
                    ft.ElevatedButton("Sair (0)", on_click=exit_drop)
                ])
            )
            self.page.update()

    # --- Manipuladores do Menu Principal ---
    def show_main_menu():
        """Exibe o menu principal na UI."""
        output_area.controls.clear() # Limpa a área de saída
        output_area.controls.append(main_menu_display)
        output_area.controls.append(main_input_field)
        output_area.controls.append(ft.Text("*--------------------------------------------*"))
        main_input_field.value = "" # Limpa o campo de entrada principal
        page.update()

    def handle_main_menu_selection(value):
        """Lida com a seleção de opção do menu principal."""
        try:
            op = int(value)
            main_input_field.value = "" # Limpa o campo de entrada após a seleção
            
            # Callback para retornar ao menu principal após uma operação CRUD
            def return_to_main_menu():
                show_main_menu()

            match op:
                case 1:
                    create_instance = Create(page, db_connection, db_cursor, output_area, return_to_main_menu)
                    create_instance.show_create_ui()
                case 2:
                    select_instance = Select(page, db_connection, db_cursor, output_area, return_to_main_menu)
                    select_instance.show_select_ui()
                case 3:
                    update_instance = Update(page, db_connection, db_cursor, output_area, return_to_main_menu)
                    update_instance.show_update_ui()
                case 4:
                    delete_instance = Delete(page, db_connection, db_cursor, output_area, return_to_main_menu)
                    delete_instance.show_delete_ui()
                case 5:
                    drop_instance = Drop(page, db_connection, db_cursor, output_area, return_to_main_menu)
                    drop_instance.show_drop_ui()
                case 0:
                    status_text.value = "Fechando a conexão e saindo..."
                    status_text.color = Colors.BLUE_700 # Changed to Colors.BLUE_700
                    page.update()
                    if db_connection and db_connection.is_connected():
                        db_cursor.close()
                        db_connection.close()
                        status_text.value = "Conexão com o banco de dados fechada."
                        status_text.color = Colors.GREEN_700 # Changed to Colors.GREEN_700
                        page.update()
                    page.window_destroy() # Fecha a janela do Flet
                case _:
                    output_area.controls.append(ft.Text("Opção inválida. Tente novamente.", color=Colors.RED_500)) # Changed to Colors.RED_500
                    page.update()
        except ValueError:
            output_area.controls.append(ft.Text("Entrada inválida. Por favor, digite um número.", color=Colors.RED_500)) # Changed to Colors.RED_500
            page.update()

    # Configuração inicial da UI na página
    page.add(
        ft.Column([
            status_text, # Exibe o status da conexão
            main_menu_display, # O texto do menu principal
            ft.Row([
                main_input_field, # Campo para digitar a opção
                ft.ElevatedButton("Confirmar", on_click=lambda e: handle_main_menu_selection(main_input_field.value)) # Botão de confirmação
            ]),
            ft.Text("*--------------------------------------------*"),
            output_area # Esta coluna será atualizada dinamicamente com as interfaces das operações CRUD
        ])
    )

# Executa o aplicativo Flet
if __name__ == "__main__":
    ft.app(target=main)