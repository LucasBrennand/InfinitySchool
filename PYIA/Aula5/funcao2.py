#Atividade 1
print("")
print("Atividade 1")
nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma nota: "))
nota3 = float(input("Digite uma nota: "))

def calcularMedia(a, b, c):
    media = (a + b + c) / 3
    print (media)
    return media

calcularMedia(nota1, nota2, nota3)

#Atividade 2
print("")
print("Atividade 2")
largura = float(input("Digite a largura: "))
comprimento = float(input("Digite o comprimento: "))

def calcularArea(a, b):
    area = (a + b) / 2
    print (area)
    return area

calcularArea(largura, comprimento)


#Atividade 3
print("")
print("Atividade 3")

def concatenarString(*args):
    resultado = ""
    for i in args:
        resultado += i
    return resultado

print(concatenarString("Ola", "Mundo", "!"))


#Atividade 4
print("")
print("Atividade 4")

def dobrarValor(valor):
    return valor * 2

def dobrarNumeros(*args):
    dobrado = list(map(dobrarValor, args))
    return dobrado

print(dobrarNumeros(1, 2, 3, 4, 5))


#Atividade 5
print("")
print("Atividade 5")

def filtrar(valor):
    if (valor % 2 == 0):
        return valor
    
def filtrarNumeros(*args):
    filtrado = list(filter(filtrar, args))
    return filtrado

print(filtrarNumeros(1, 2, 3, 4, 5, 6, 7, 8))

#Atividade 6
print("")
print("Atividade 6")

from functools import reduce

def reduzir(valor1, valor2):
    if len(valor1) > len(valor2):
        return valor1
    else:
        return valor2

def reduzirNumeros(*args):
    reduzido = reduce(reduzir, args)
    return reduzido

print(reduzirNumeros("Miguel", "Lucas", "João", "Mia", "Jonathan"))

#Atividade 7
print("")
print("Atividade 7")

def criar_lista_de_compras(*args):
    lista = args
    print(lista)

criar_lista_de_compras("Roupa","Carne","Frutas","Verduras")

#Atividade 8
print("")
print("Atividade 8")

soma = lambda a,b : a + b
sub = lambda a,b : a - b
mult = lambda a,b : a * b
div = lambda a,b : a / b
print(soma(5, 2))
print(sub(7, 6))
print(mult(3, 5))
print(div(9, 3))

#Desafio
print("")
print("Desafio")