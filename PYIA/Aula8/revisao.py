# Atividade 1
print("Atividade 1")      
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_dobrada = list(filter(lambda x: x % 2 == 0, numeros))
print(lista_dobrada)

# Atividade 2
print("Atividade 2")  
produtos = {
    "nome": "Banana",
    "preco": 5.50,
    "quantidade": 10
} 

def mudar_preco():
    produtos["preco"] = 6.50

def mudar_quantidade():
    produtos["quantidade"] = 20

def remover_preco():
    del produtos["preco"]

mudar_preco()
remover_preco()
print(produtos)

# Atividade 3
print("Atividade 3") 
cores = {"Azul", "Vermelho", "Amarelo", "Rosa", "Ciano", "Ciano", "Marfim"}

cores_com_mais_quatro_letras = list(filter(lambda x: len(x) > 4, cores))
print(cores_com_mais_quatro_letras)

# Atividade 4
print("Atividade 4") 
lista_palavras = ["madam", "toot", "miguel", "jaum", "bruna"]

def inverter_string():
    reversed_string = lista_palavras[::-1]
    print(reversed_string)
    return reversed_string

def palindromo():
    palavra_invertida = inverter_string()
    print(palavra_invertida)
    for i in lista_palavras:
        if (i == palavra_invertida):
            print(f"{i} é um palindromo")
            return i
        else:
            print("Não é um palindromo")

palindromo()