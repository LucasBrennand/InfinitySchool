#Atv1
# Solicitar a idade do usuário
idade = int(input("Digite sua idade: "))

# Classificar a pessoa com base na idade
if idade < 12:
    print("Criança")
elif 12 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
else:
    print("Idoso")



#Atv2
# Solicitar ao usuário que digite 3 números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Encontrar o maior e o menor número
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

# Exibir os resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")



#Atv3
# Inicializando as variáveis para contar os números pares e ímpares
pares = 0
impares = 0

# Pedindo ao usuário para inserir 10 números inteiros
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    
    # Verificando se o número é par ou ímpar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibindo o resultado
print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")



#Atv4
# Solicitar o número de pessoas
n = int(input("Digite o número de pessoas: "))

# Inicializando a variável para armazenar a soma das idades
soma_idades = 0

# Solicitar a idade de cada pessoa e acumular a soma das idades
for i in range(n):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    soma_idades += idade

# Calcular a média das idades
media_idade = soma_idades / n

# Classificar a turma com base na média de idades
if media_idade <= 25:
    print("A turma é jovem.")
elif 26 <= media_idade <= 60:
    print("A turma é adulta.")
else:
    print("A turma é idosa.")

# Exibir a média de idade
print(f"A média de idade da turma é: {media_idade:.2f}")



#Atv5
# Solicitar o número de elementos do conjunto
n = int(input("Digite o número de elementos: "))

# Inicializando uma lista para armazenar os números
numeros = []

# Recebendo os números do usuário
for i in range(n):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Determinando o menor valor, o maior valor e a soma dos valores
menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

# Exibindo os resultados
print(f"O menor valor é: {menor}")
print(f"O maior valor é: {maior}")
print(f"A soma dos valores é: {soma}")

#AtvPratica
# Inicializando variáveis para o total gasto, contador de produtos caros e o produto mais barato
total_gasto = 0
produtos_caros = 0
produto_mais_barato = ""
preco_mais_barato = float('inf')  # Inicializando com um valor muito alto

# Laço para continuar inserindo produtos enquanto o usuário quiser
while True:
    # Solicitar nome e preço do produto
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto (R$): "))
    
    # Atualizar o total gasto
    total_gasto += preco
    
    # Verificar se o produto custa mais de R$1000
    if preco > 1000:
        produtos_caros += 1
    
    # Verificar se é o produto mais barato
    if preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome
    
    # Perguntar se o usuário quer continuar
    continuar = input("Deseja adicionar mais produtos? (sim/não): ").strip().lower()
    if continuar != "sim":
        break

# Exibir o resumo da compra
print("\nResumo da Compra:")
print(f"Total gasto: R${total_gasto:.2f}")
print(f"Quantidade de produtos que custam mais de R$1000: {produtos_caros}")
print(f"Produto mais barato: {produto_mais_barato} - R${preco_mais_barato:.2f}")
