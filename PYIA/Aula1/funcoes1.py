#Atv1
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

# Exemplo de uso
nome_usuario = input("Digite seu nome: ")
saudacao(nome_usuario)

#Atv2
def saudacao_por_horario(hora):
    if 0 <= hora < 12:
        print("Bom dia!")
    elif 12 <= hora < 18:
        print("Boa tarde!")
    elif 18 <= hora <= 23:
        print("Boa noite!")
    else:
        print("Hora inválida. Digite um valor entre 0 e 23.")

# Exemplo de uso
hora_informada = int(input("Digite a hora atual (0 a 23): "))
saudacao_por_horario(hora_informada)

#Atv3
def somar(a, b):
    return a + b

# Exemplo de uso
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = somar(num1, num2)
print(f"A soma é: {resultado}")


#Atv4
def subtrair(a, b):
    return a - b

# Exemplo de uso
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = subtrair(num1, num2)
print(f"A subtração é: {resultado}")


#Atv5
def multiplicar(a, b):
    return a * b

# Exemplo de uso
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = multiplicar(num1, num2)
print(f"A multiplicação é: {resultado}")


#AtvPratica
# Funções de operação
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

# Função principal (menu)
def calculadora():
    while True:
        print("\n=== CALCULADORA ===")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Encerrando a calculadora. Até logo!")
            break

        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Use apenas números.")
                continue

            if opcao == '1':
                resultado = somar(num1, num2)
            elif opcao == '2':
                resultado = subtrair(num1, num2)
            elif opcao == '3':
                resultado = multiplicar(num1, num2)
            elif opcao == '4':
                resultado = dividir(num1, num2)

            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida. Tente novamente.")

# Executa a calculadora
calculadora()

