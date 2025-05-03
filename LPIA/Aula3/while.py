# #Atv 1
# contador = 1
# while (contador <= 100):
#     print(f"O número do contador é {contador}")
#     contador+=1

# #Atv 4
# contador = 10
# while (contador != -1):
#     if (contador == 0):
#         print(f"Feliz ano novo!")
#         break
#     print(f"O número do contador é {contador}")
#     contador-=1

#Atv 5
# contador = 1
# num = int(input("Digite um número: "))

# while (contador <= num):
#     if(contador % 2 == 1):
#         print(f"Numero {contador}")
#     contador+=1

# #Atv 6
# contador = 1
# num = int(input("Digite um número: "))
# currentNum = 0

# while (num >= 0):
#     print(f"Número escolhido: {num}")
#     currentNum = currentNum + num
#     print(f"Valor atual: {currentNum}")
#     num = int(input("Digite outro número: "))

# #Atv 8
contador = 0
nota = 0
num = 0
novaNota = 0
media = 0

while (num != -1):
    num = float(input("Digite uma nota: "))
    if (num == -1):
        print(f"Saindo")
        break
    else:
        novaNota = novaNota + num
        contador+=1
        media = novaNota / contador
        print(f"A média é {media}")
