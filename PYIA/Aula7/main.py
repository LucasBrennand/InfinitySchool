from module import input_numeros, soma, subtracao, multiplicacao, divisao
from manipulacao_strings import inverter_string, contar_palavras, palindromo
from math_defs import calcular_area
from random_def import advinhar_numero
from pytemp import pytemp
from biblioteca import adicionar_livro, verificar_disponibilidade, listar_livros, devolver_livro, emprestimo_livro, livros

# # Atividade 1
# print("Atividade 1")
# op = 1

# while (op != 0):
#     numeros = input_numeros()
#     op = int(input("""O que você quer fazer?
#                    1. Somar
#                    2. Subtrair
#                    3. Multiplicar
#                    4. Dividir
#                    0. Sair
#                     """))
#     match (op):
#         case 1:
#             soma(numeros)
#         case 2:
#             subtracao(numeros)
#         case 3:
#             multiplicacao(numeros)
#         case 4:
#             divisao(numeros)
#         case 0:
#             print("Saindo...")
#         case _:
#             print("Opção inválida")

# # Atividade 2
# # print("Atividade 2")
# # inverter_string("Hello World")
# # contar_palavras("Olá, meu nome é Lucas")
# palindromo("madam")

# # Atividade 3
# print("Atividade 3")
# calcular_area(4.3, 2.4, 3.8)

# # Atividade 4
# print("Atividade 4")
# advinhar_numero()

# # Atividade 5
# print("Atividade 5")
# celsius = 25
# fahrenheit = pytemp(celsius, 'celsius', 'fahrenheit')
# print(f"{celsius} é igual {fahrenheit}")

# Desafio
# main.py
print("Desafio")
op = 1

while (op != 0):
    op = int(input("""O que você quer fazer?
                   1. Adicionar um livro
                   2. Listar os livros
                   3. Verificar a disponibilidade de um livro
                   4. Pegar um livro emprestado
                   5. Devolver um livro
                   0. Sair
                    """))
    match (op):
        case 1:
            adicionar_livro()
        case 2:
            listar_livros()
        case 3:
            verificar_disponibilidade()
        case 4:
            emprestimo_livro()
        case 5:
            devolver_livro()
        case 0:
            print("Saindo...")
        case _:
            print("Opção inválida")