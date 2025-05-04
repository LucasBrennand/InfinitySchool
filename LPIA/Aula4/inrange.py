# num = int(input("Digite um número: "))
# for i in range(num):
#     print(i)

# num = 50
# for i in range(1, 10, 3):
#     print(i)

# #Atv2
# soma = 0
# for i in range(1, 101):
#     soma += i
#     print(soma)


# #Atv3
# palavra = input("Digite uma palavra: ")
# for i in palavra:
#     print(i)


# # #Atv4
# for i in range(10, -1, -1):
#     print(i)
#     if(i == 0):
#         print("Feliz Ano novo!")

# # #Atv6
# soma = 0
# for i in range(1, 51):
#     if (i % 2 == 0):
#         soma += i
#         print(soma)


# # # #Atv7
# a = 0
# e = 0
# i1 = 0
# o = 0
# u = 0
# palavra = input("Digite uma palavra: ")
# for i in palavra:
#     if (i == "a"):
#         a += 1
#     elif (i == "e"):
#         e += 1
#     elif (i == "i"):
#         i1 += 1
#     elif (i == "o"):
#         o += 1
#     elif (i == "u"):
#         u += 1
# print(f"Quantidade da letra A: {a}")
# print(f"Quantidade da letra E: {e}")
# print(f"Quantidade da letra I: {i1}")
# print(f"Quantidade da letra O {o}")
# print(f"Quantidade da letra U: {u}")

# # # # #Atv8
# soma = 0
# media = 0
# for i in range(1, 6):
#     num = int(input("Digite uma nota: "))
#     print(f"Nota {i}: {num}")
#     soma += num
#     media = soma / 5
#     print(f"A média é {media}")

#     if (media >= 6):
#         print("Aprovado")
#     else:
#         print("Reprovado")

# # # # # #Atv9
# for i in range(1, 21):
#     if (i % 2 == 0):
#         print(f"Número {i} é par")
#     elif(i == 15):
#         print(f"{i} detectado, saindo..")
#         break
#     else:
#         print(f"Número {i} é ímpar")

# # # # #Atv11
for i in range(1, 31):
    if (i > 20):
        print("Maior que 20, saindo..")
        break
    if (i % 5 == 0):
        print(f"Número {i} é multiplo de 5")
