from module import input_numeros, soma, subtracao, multiplicacao, divisao

op = 1

while (op != 0):
    numeros = input_numeros()
    op = int(input("""O que você quer fazer?
                   1. Somar
                   2. Subtrair
                   3. Multiplicar
                   4. Dividir
                   0. Sair
                    """))
    match (op):
        case 1:
            soma(numeros)
        case 2:
            subtracao(numeros)
        case 3:
            multiplicacao(numeros)
        case 4:
            divisao(numeros)
        case 0:
            print("Saindo...")
        case _:
            print("Opção inválida")
