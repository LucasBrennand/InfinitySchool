#Atv1
# operacoes.py

def soma(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtracao(a, b):
    """Retorna a subtração de a e b."""
    return a - b

def multiplicacao(a, b):
    """Retorna a multiplicação de a e b."""
    return a * b

def divisao(a, b):
    """Retorna a divisão de a por b. Se b for zero, retorna uma mensagem de erro."""
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b


#Atv2
# manipulacao_strings.py
def inverter_string(s):
    """Retorna a string invertida."""
    return s[::-1]

def contar_palavras(s):
    """Retorna o número de palavras em uma string."""
    palavras = s.split()
    return len(palavras)

def eh_palindromo(s):
    """Verifica se a string é um palíndromo (lê-se igual de trás para frente)."""
    s = s.replace(" ", "").lower()  # Remove espaços e converte para minúsculo
    return s == s[::-1]

# programa_principal.py
import manipulacao_strings as ms

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("Escolha uma operação:")
    print("1. Inverter a string")
    print("2. Contar o número de palavras")
    print("3. Verificar se é um palíndromo")
    print("4. Sair")

def obter_string():
    """Obtém uma string do usuário."""
    return input("Digite uma string: ")

def obter_opcao():
    """Obtém a opção do usuário."""
    while True:
        try:
            opcao = int(input("Escolha a opção desejada (1-4): "))
            if opcao in [1, 2, 3, 4]:
                return opcao
            else:
                print("Opção inválida! Digite um número entre 1 e 4.")
        except ValueError:
            print("Por favor, digite um número válido.")

def executar():
    """Função principal que chama as funções do módulo conforme a escolha do usuário."""
    while True:
        exibir_menu()
        opcao = obter_opcao()

        if opcao == 1:
            s = obter_string()
            resultado = ms.inverter_string(s)
            print(f"A string invertida é: {resultado}\n")
        
        elif opcao == 2:
            s = obter_string()
            resultado = ms.contar_palavras(s)
            print(f"A quantidade de palavras na string é: {resultado}\n")
        
        elif opcao == 3:
            s = obter_string()
            if ms.eh_palindromo(s):
                print("A string é um palíndromo!\n")
            else:
                print("A string não é um palíndromo.\n")
        
        elif opcao == 4:
            print("Saindo do programa. Até logo!")
            break

if __name__ == "__main__":
    executar()


#Atv3
import math

def calcular_area_quadrado(lado):
    """Calcula a área de um quadrado."""
    return lado ** 2

def calcular_perimetro_quadrado(lado):
    """Calcula o perímetro de um quadrado."""
    return 4 * lado

def calcular_area_retangulo(comprimento, largura):
    """Calcula a área de um retângulo."""
    return comprimento * largura

def calcular_perimetro_retangulo(comprimento, largura):
    """Calcula o perímetro de um retângulo."""
    return 2 * (comprimento + largura)

def calcular_area_circulo(raio):
    """Calcula a área de um círculo."""
    return math.pi * raio ** 2

def calcular_perimetro_circulo(raio):
    """Calcula o perímetro (circunferência) de um círculo."""
    return 2 * math.pi * raio

def exibir_menu():
    """Exibe o menu para o usuário escolher a forma geométrica."""
    print("\nEscolha a forma geométrica:")
    print("1. Quadrado")
    print("2. Retângulo")
    print("3. Círculo")
    print("4. Sair")

def obter_opcao():
    """Obtém a opção do usuário."""
    while True:
        try:
            opcao = int(input("Escolha a opção desejada (1-4): "))
            if 1 <= opcao <= 4:
                return opcao
            else:
                print("Opção inválida! Digite um número entre 1 e 4.")
        except ValueError:
            print("Por favor, digite um número válido.")

def obter_valores_quadrado():
    """Obtém o valor do lado do quadrado."""
    lado = float(input("Digite o comprimento do lado do quadrado: "))
    return lado

def obter_valores_retangulo():
    """Obtém os valores do comprimento e largura do retângulo."""
    comprimento = float(input("Digite o comprimento do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    return comprimento, largura

def obter_valores_circulo():
    """Obtém o valor do raio do círculo."""
    raio = float(input("Digite o raio do círculo: "))
    return raio

def executar():
    """Função principal que gerencia o menu e executa as operações."""
    while True:
        exibir_menu()
        opcao = obter_opcao()

        if opcao == 1:
            lado = obter_valores_quadrado()
            area = calcular_area_quadrado(lado)
            perimetro = calcular_perimetro_quadrado(lado)
            print(f"A área do quadrado é: {area:.2f}")
            print(f"O perímetro do quadrado é: {perimetro:.2f}\n")

        elif opcao == 2:
            comprimento, largura = obter_valores_retangulo()
            area = calcular_area_retangulo(comprimento, largura)
            perimetro = calcular_perimetro_retangulo(comprimento, largura)
            print(f"A área do retângulo é: {area:.2f}")
            print(f"O perímetro do retângulo é: {perimetro:.2f}\n")

        elif opcao == 3:
            raio = obter_valores_circulo()
            area = calcular_area_circulo(raio)
            perimetro = calcular_perimetro_circulo(raio)
            print(f"A área do círculo é: {area:.2f}")
            print(f"O perímetro (circunferência) do círculo é: {perimetro:.2f}\n")

        elif opcao == 4:
            print("Saindo do programa. Até logo!")
            break

if __name__ == "__main__":
    executar()


#Atv4
import random

def jogar_adivinhacao():
    print("🎯 Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.\n")

    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("🔺 O número é MAIOR que isso.")
            elif palpite > numero_secreto:
                print("🔻 O número é MENOR que isso.")
            else:
                print(f"✅ Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
                break
        except ValueError:
            print("❗ Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    jogar_adivinhacao()

#Atv5
# conversoes.py

def metros_para_pes(metros):
    return metros * 3.28084

def quilogramas_para_libras(kg):
    return kg * 2.20462

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

# conversor_principal.py

import conversoes

def menu():
    print("\n=== Conversor de Unidades ===")
    print("1. Metros para Pés")
    print("2. Quilogramas para Libras")
    print("3. Celsius para Fahrenheit")
    print("0. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        metros = float(input("Digite o valor em metros: "))
        pes = conversoes.metros_para_pes(metros)
        print(f"{metros} metros equivalem a {pes:.2f} pés.")
    elif opcao == "2":
        kg = float(input("Digite o valor em quilogramas: "))
        libras = conversoes.quilogramas_para_libras(kg)
        print(f"{kg} kg equivalem a {libras:.2f} libras.")
    elif opcao == "3":
        c = float(input("Digite a temperatura em Celsius: "))
        f = conversoes.celsius_para_fahrenheit(c)
        print(f"{c}°C equivalem a {f:.2f}°F.")
    elif opcao == "0":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

#Desafio
# Gerenciador de Livros de Biblioteca

biblioteca = {}
emprestimos = {}

def adicionar_livro():
    titulo = input("Título do livro: ").strip()
    autor = input("Autor do livro: ").strip()
    copias = int(input("Número de cópias disponíveis: "))

    if titulo in biblioteca:
        biblioteca[titulo]['copias'] += copias
    else:
        biblioteca[titulo] = {'autor': autor, 'copias': copias}
    
    print(f"Livro '{titulo}' adicionado com sucesso.")

def listar_livros():
    print("\n=== Livros disponíveis ===")
    if not biblioteca:
        print("Nenhum livro cadastrado.")
    else:
        for titulo, info in biblioteca.items():
            print(f"Título: {titulo} | Autor: {info['autor']} | Cópias: {info['copias']}")

def emprestar_livro():
    usuario = input("Nome do usuário: ").strip()
    titulo = input("Título do livro que deseja emprestar: ").strip()

    if titulo in biblioteca and biblioteca[titulo]['copias'] > 0:
        biblioteca[titulo]['copias'] -= 1
        emprestimos.setdefault(usuario, []).append(titulo)
        print(f"{usuario} emprestou '{titulo}'.")
    else:
        print("Livro não disponível ou não encontrado.")

def devolver_livro():
    usuario = input("Nome do usuário: ").strip()
    titulo = input("Título do livro que deseja devolver: ").strip()

    if usuario in emprestimos and titulo in emprestimos[usuario]:
        emprestimos[usuario].remove(titulo)
        biblioteca[titulo]['copias'] += 1
        print(f"{usuario} devolveu '{titulo}'.")
    else:
        print("Esse empréstimo não foi encontrado.")

def verificar_disponibilidade():
    titulo = input("Título do livro: ").strip()
    if titulo in biblioteca:
        print(f"Cópias disponíveis de '{titulo}': {biblioteca[titulo]['copias']}")
    else:
        print("Livro não encontrado.")

def mostrar_livros_usuario():
    usuario = input("Nome do usuário: ").strip()
    if usuario in emprestimos and emprestimos[usuario]:
        print(f"\n{usuario} emprestou os seguintes livros:")
        for livro in emprestimos[usuario]:
            print(f"- {livro}")
    else:
        print(f"{usuario} não possui livros emprestados.")

def menu():
    print("\n=== MENU BIBLIOTECA ===")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Verificar disponibilidade de livro")
    print("6. Ver livros emprestados por usuário")
    print("0. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_livro()
    elif escolha == "2":
        listar_livros()
    elif escolha == "3":
        emprestar_livro()
    elif escolha == "4":
        devolver_livro()
    elif escolha == "5":
        verificar_disponibilidade()
    elif escolha == "6":
        mostrar_livros_usuario()
    elif escolha == "0":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

