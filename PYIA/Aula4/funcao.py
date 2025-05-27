#Atividade 1
print("")
print("Atividade 1")

def helloWorld(nome):
    print(f"Ola {nome}")

helloWorld("Lucas")

#Atividade 2
print("")
print("Atividade 2")

from datetime import datetime

print(datetime)
date = datetime(year = 2025, month = 5, day = 27, hour = 18)
if (date.hour > 4 and date.hour < 12):
    print(f"Bom dia! Hoje é {date.year, date.month, date.day}")
elif (date.hour >= 12 and date.hour < 18):
    print(f"Boa tarde! Hoje é {date.year, date.month, date.day}")
else:
    print(f"Boa noite! Hoje é {date.year, date.month, date.day}")

#Atividade 3
print("")
print("Atividade 3")

def soma(a, b):
    return a + b

print(soma(5, 3))

#Atividade 4
print("")
print("Atividade 4")

def subtracao(a, b):
    return a - b

print(subtracao(10, 4))

#Atividade 5
print("")
print("Atividade 5")

def mult(a, b):
    return a * b

print(mult(5, 2))

#Prática
print("")
print("Prática")

def div(a, b):
    return a / b

def numInput():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    return a, b

while(True):
    op = int(input(f"Digite uma opção: \n1.Soma \n2.Subtração \n3.Multiplicação \n4.Divisão \n5.Sair \n=> "))
    if (op == 1):
        a, b = numInput()
        print(f"Soma: {soma(a, b)}")

    elif (op == 2):
        a, b = numInput()
        print(f"Subtração: {subtracao(a, b)}")

    elif (op == 3):
        a, b = numInput()
        print(f"Multiplicação: {mult(a, b)}")

    elif (op == 4):
        a, b = numInput()
        print(f"Divisão: {div(a, b)}")

    elif (op == 5):
        print("Saindo..")
        break

    else:
        print("Opção inválida")
  