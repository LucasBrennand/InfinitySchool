#Atv1
def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filtrar_pares(numeros)

print("Números pares:", pares)

#Atv2
# Dicionário para armazenar os produtos
produtos = {}

# Função para adicionar um produto
def adicionar_produto(nome, preco, quantidade):
    produtos[nome] = {"preco": preco, "quantidade": quantidade}
    print(f"Produto '{nome}' adicionado com sucesso.")

# Função para remover um produto
def remover_produto(nome):
    if nome in produtos:
        del produtos[nome]
        print(f"Produto '{nome}' removido com sucesso.")
    else:
        print(f"Produto '{nome}' não encontrado.")

# Função para atualizar um produto
def atualizar_produto(nome, preco=None, quantidade=None):
    if nome in produtos:
        if preco is not None:
            produtos[nome]["preco"] = preco
        if quantidade is not None:
            produtos[nome]["quantidade"] = quantidade
        print(f"Produto '{nome}' atualizado com sucesso.")
    else:
        print(f"Produto '{nome}' não encontrado.")

# Exemplo de uso
adicionar_produto("Caneta", 2.5, 100)
adicionar_produto("Caderno", 10.0, 50)
atualizar_produto("Caneta", preco=2.8)
remover_produto("Caderno")

# Mostrar os produtos
print("\nEstoque atual:")
for nome, info in produtos.items():
    print(f"{nome}: Preço: R${info['preco']:.2f}, Quantidade: {info['quantidade']}")


#Atv3
# Conjunto com nomes de cores
cores = {"azul", "verde", "vermelho", "rosa", "roxo", "amarelo", "preto", "branco"}

# Função que retorna as cores com mais de 4 letras
def cores_com_mais_de_quatro_letras(conjunto_cores):
    return {cor for cor in conjunto_cores if len(cor) > 4}

# Chamando a função e exibindo o resultado
resultado = cores_com_mais_de_quatro_letras(cores)
print("Cores com mais de 4 letras:", resultado)


#Atv4
# Função que verifica se uma string é um palíndromo
def encontrar_palindromos(lista_strings):
    return [palavra for palavra in lista_strings if palavra == palavra[::-1]]

# Exemplo de uso
lista = ["ana", "python", "radar", "civic", "palavra", "arara"]
resultado = encontrar_palindromos(lista)

print("Palíndromos encontrados:", resultado)

#Atv5
def produtos_mais_vendidos(vendas):
    max_vendas = max(vendas.values())
    mais_vendidos = [produto for produto, quantidade in vendas.items() if quantidade == max_vendas]
    return mais_vendidos

# Exemplo de dicionário de vendas
vendas = {
    "Camiseta": 120,
    "Calça": 75,
    "Tênis": 120,
    "Boné": 90
}

resultado = produtos_mais_vendidos(vendas)

print("Produto(s) mais vendido(s):", resultado)

#Atv6
def contar_pares_impares(lista):
    pares = sum(1 for num in lista if num % 2 == 0)
    impares = sum(1 for num in lista if num % 2 != 0)
    return pares, impares

# Exemplo de uso
numeros = [10, 3, 4, 7, 8, 15, 22, 17, 6, 9]

qtd_pares, qtd_impares = contar_pares_impares(numeros)

print("Quantidade de números pares:", qtd_pares)
print("Quantidade de números ímpares:", qtd_impares)


#Atv7
def calcular_media_trimestres(vendas_trimestrais):
    medias = []
    for i, trimestre in enumerate(vendas_trimestrais):
        media = sum(trimestre) / len(trimestre)
        medias.append(media)
        print(f"Média de vendas do {i+1}º trimestre: {media:.2f}")
    return medias

# Exemplo de dados: 4 trimestres, cada um com 3 meses
vendas = [
    [10000, 12000, 11000],  # Jan-Mar
    [13000, 12500, 14000],  # Abr-Jun
    [15000, 16000, 15500],  # Jul-Set
    [17000, 16500, 18000]   # Out-Dez
]

# Executando a função
calcular_media_trimestres(vendas)


#Atv8
def analisar_vendas_trimestres(vendas_trimestrais):
    somas = [sum(trimestre) for trimestre in vendas_trimestrais]
    
    maior_soma = max(somas)
    menor_soma = min(somas)
    
    trimestre_maior = somas.index(maior_soma) + 1
    trimestre_menor = somas.index(menor_soma) + 1
    
    total_vendas_ano = sum(somas)
    
    print(f"Total de vendas no ano: {total_vendas_ano}")
    print(f"Trimestre com maior soma de vendas: {trimestre_maior}º trimestre - {maior_soma}")
    print(f"Trimestre com menor soma de vendas: {trimestre_menor}º trimestre - {menor_soma}")

# Exemplo de dados: 4 trimestres, cada um com 3 meses
vendas = [
    [10000, 12000, 11000],  # Jan-Mar
    [13000, 12500, 14000],  # Abr-Jun
    [15000, 16000, 15500],  # Jul-Set
    [17000, 16500, 18000]   # Out-Dez
]

# Executando a função
analisar_vendas_trimestres(vendas)


#Desafio
def analisar_producao(producao):
    anos = list(producao.keys())
    culturas = list(producao[anos[0]].keys())  # Considerando que todas as fazendas têm as mesmas culturas
    
    # Tarefa 1: Ano com produção máxima e mínima
    producao_anos = {ano: sum(producao[ano].values()) for ano in anos}
    ano_max = max(producao_anos, key=producao_anos.get)
    ano_min = min(producao_anos, key=producao_anos.get)
    
    # Tarefa 2: Cultura com maior e menor produção total
    producao_culturas = {cultura: sum(producao[ano][cultura] for ano in anos) for cultura in culturas}
    cultura_max = max(producao_culturas, key=producao_culturas.get)
    cultura_min = min(producao_culturas, key=producao_culturas.get)
    
    # Tarefa 3: Fazendas com produção máxima e mínima em um ano específico (escolha de ano, ex: 2021)
    ano_especifico = 2021
    fazendas_ano = producao[ano_especifico]
    fazenda_max = max(fazendas_ano, key=fazendas_ano.get)
    fazenda_min = min(fazendas_ano, key=fazendas_ano.get)
    
    # Resultados
    print(f"Ano com a maior produção: {ano_max} ({producao_anos[ano_max]} unidades)")
    print(f"Ano com a menor produção: {ano_min} ({producao_anos[ano_min]} unidades)")
    
    print(f"Cultura com a maior produção: {cultura_max} ({producao_culturas[cultura_max]} unidades)")
    print(f"Cultura com a menor produção: {cultura_min} ({producao_culturas[cultura_min]} unidades)")
    
    print(f"Fazenda com a maior produção em {ano_especifico}: {fazenda_max} ({fazendas_ano[fazenda_max]} unidades)")
    print(f"Fazenda com a menor produção em {ano_especifico}: {fazenda_min} ({fazendas_ano[fazenda_min]} unidades)")

# Dados fictícios: Produção anual das fazendas para diferentes culturas
producao = {
    2020: {"Soja": 5000, "Milho": 4000, "Trigo": 3000, "Arroz": 2000},
    2021: {"Soja": 5500, "Milho": 4500, "Trigo": 3200, "Arroz": 2100},
    2022: {"Soja": 6000, "Milho": 4700, "Trigo": 3400, "Arroz": 2300},
    2023: {"Soja": 6500, "Milho": 4800, "Trigo": 3500, "Arroz": 2500}
}

# Executando a função para análise de produção
analisar_producao(producao)
