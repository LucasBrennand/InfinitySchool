#Atv1
# Função que calcula a média
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Chamada da função
media = calcular_media(nota1, nota2, nota3)

# Saída
print(f"A média das notas é: {media:.2f}")


#Atv2
# Função que calcula a área do retângulo
def calcular_area_retangulo(comprimento, largura):
    return comprimento * largura

# Entrada de dados
comprimento = float(input("Digite o comprimento do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))

# Chamada da função e exibição do resultado
area = calcular_area_retangulo(comprimento, largura)
print(f"A área do retângulo é: {area:.2f}")

#Atv3
# Função que concatena várias strings
def concatenar_strings(*args):
    return ''.join(args)

# Exemplo de uso
resultado = concatenar_strings("Olá, ", "mundo", "! ", "Como ", "vai?")
print("Resultado da concatenação:", resultado)


#Atv4
# Função que dobra cada número da lista
def dobrar_numeros(lista):
    return list(map(lambda x: x * 2, lista))

# Exemplo de uso
numeros = [1, 2, 3, 4, 5]
resultado = dobrar_numeros(numeros)
print("Lista com os números dobrados:", resultado)


#Atv5
# Função que filtra números pares
def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_pares(numeros)
print("Lista com os números pares:", resultado)


#Atv6
from functools import reduce

# Função que encontra a maior string usando reduce
def maior_string(lista):
    return reduce(lambda a, b: a if len(a) > len(b) else b, lista)

# Exemplo de uso
strings = ["maçã", "banana", "abacaxi", "laranja"]
resultado = maior_string(strings)
print("A maior string é:", resultado)


#Atv7
# Função que cria uma lista de compras com base nos itens fornecidos
def criar_lista_de_compras(*itens):
    return list(itens)

# Exemplo de uso
lista = criar_lista_de_compras("Arroz", "Feijão", "Macarrão", "Leite", "Ovos")
print("Lista de compras:", lista)


#Atv8
# Função que realiza a operação especificada
def calcular_operacao(num1, num2, operacao):
    # Dicionário de operações com funções lambda
    operacoes = {
        'soma': lambda x, y: x + y,
        'subtracao': lambda x, y: x - y,
        'multiplicacao': lambda x, y: x * y,
        'divisao': lambda x, y: x / y if y != 0 else 'Erro: divisão por zero'
    }
    
    # Executa a operação
    return operacoes.get(operacao, lambda x, y: 'Operação inválida')(num1, num2)

# Exemplo de uso
resultado = calcular_operacao(10, 5, 'multiplicacao')
print(f"O resultado da operação é: {resultado}")


#AtvPratica
# Função que processa o texto de acordo com as operações especificadas
def processador_texto(texto, **operacoes):
    # Operação para contar palavras
    contar_palavras = lambda texto: len(texto.split())
    
    # Operação para contar letras
    contar_letras = lambda texto: sum(len(palavra) for palavra in texto.split())
    
    # Operação para inverter o texto
    inverter_texto = lambda texto: texto[::-1]
    
    # Operação para substituir uma palavra
    substituir_palavra = lambda texto, velha_palavra, nova_palavra: texto.replace(velha_palavra, nova_palavra)
    
    # Processando as operações solicitadas
    if 'contar_palavras' in operacoes and operacoes['contar_palavras']:
        print(f"Quantidade de palavras: {contar_palavras(texto)}")
    
    if 'contar_letras' in operacoes and operacoes['contar_letras']:
        print(f"Quantidade de letras: {contar_letras(texto)}")
    
    if 'inverter_texto' in operacoes and operacoes['inverter_texto']:
        print(f"Texto invertido: {inverter_texto(texto)}")
    
    if 'substituir_palavra' in operacoes and operacoes['substituir_palavra']:
        velha_palavra = operacoes['substituir_palavra']
        nova_palavra = operacoes.get('nova_palavra', '')
        texto = substituir_palavra(texto, velha_palavra, nova_palavra)
        print(f"Texto após substituição: {texto}")
    
    return texto

# Exemplo de uso
texto_inicial = "O Python é uma linguagem poderosa e versátil."

# Chamando a função com operações diferentes
processador_texto(
    texto_inicial, 
    contar_palavras=True, 
    contar_letras=True, 
    inverter_texto=True, 
    substituir_palavra="Python", 
    nova_palavra="Java"
)

