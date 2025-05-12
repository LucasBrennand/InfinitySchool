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
