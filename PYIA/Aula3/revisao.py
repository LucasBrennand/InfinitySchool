#Atividade 1
print("")
print("Atividade 1")

idade = int(input("Digite sua idade: "))
if (idade < 12):
    print("Criança")
elif (idade >= 12 and idade <= 17):
    print("Adolescente")
elif (idade >= 18):
    if(idade < 60):
        print("Adulto")
    else:
        print("Idoso")

#Atividade 2
print("")
print("Atividade 2")

lista = [40, 20, 75, -2, 0, 95]
maior = max(lista)
menor = min(lista)
print(maior)
print(menor)

#Atividade 3
print("")
print("Atividade 3")

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numPar = []
numImpar = []

for i in num:
    if (i % 2 == 0):
        numPar.append(i)
    else:
        numImpar.append(i)

print(numPar)
print(numImpar)

#Atividade 4
print("")
print("Atividade 4")

soma = 0
pessoas = [20, 34, 90, 65, 71, 90, 90]
for i in pessoas:
    soma = soma + i

media = soma / len(pessoas)
if (media > 0 and media <= 25):
    print("Jovem")
elif (media > 25 and media <= 60):
    print("Adulto")
else:
    print("Idoso")
print(media)

#Atividade 5
print("")
print("Atividade 5")

num = [2, 6, 3, 10, 23]
soma = 0

for i in num:
    soma = soma + i

print(soma)
print(max(num))
print(min(num))

#Desafio
print("")
print("Desafio")