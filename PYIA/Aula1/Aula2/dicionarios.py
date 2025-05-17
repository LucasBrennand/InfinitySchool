# #Atv1
# frutas = set()  # Conjunto vazio
# # Adicionando frutas
# frutas.add("maçã")
# frutas.add("banana")
# frutas.add("uva")
# frutas.add("laranja")
# frutas.add("morango")

# # Imprimindo o conjunto
# print(frutas)

# #Atv2
# # Verificando se "banana" está no conjunto
# if "banana" in frutas:
#     print("A fruta 'banana' está no conjunto.")
# else:
#     print("A fruta 'banana' não está no conjunto.")

# #Atv3
# frutas_vermelhas = {"morango", "cereja", "framboesa"}
# print(frutas_vermelhas)

# #Atv4
# frutas_vermelhas.remove("cereja")
# print(frutas_vermelhas)

# #Atv5
# # Criando os conjuntos
# A = {1, 2, 3}
# B = {3, 4, 5}

# # União dos conjuntos
# uniao = A.union(B)

# # Imprimindo o resultado
# print("União dos conjuntos A e B:", uniao)

# #Atv6
# # Criando os conjuntos
# conjunto1 = {1, 2, 3, 4}
# conjunto2 = {3, 4, 5, 6}

# # Interseção dos conjuntos
# intersecao = conjunto1.intersection(conjunto2)

# # Imprimindo o resultado
# print("Interseção dos conjuntos:", intersecao)

# #Atv7
# # Duas listas com possíveis elementos repetidos
# lista1 = [1, 2, 2, 3, 4]
# lista2 = [3, 4, 4, 5, 6]

# # Convertendo as listas em conjuntos para eliminar duplicatas
# conjunto1 = set(lista1)
# conjunto2 = set(lista2)

# # União dos conjuntos
# uniao = conjunto1.union(conjunto2)

# # Imprimindo o resultado
# print("União dos elementos únicos:", uniao)


# #Atv8
# # Dicionário com informações de pessoas
# pessoas = {
#     "Ana": 25,
#     "Bruno": 30,
#     "Carla": 22
# }

# # Exibindo as informações
# for nome, idade in pessoas.items():
#     print(f"Nome: {nome}, Idade: {idade}")


# #Atv9
# # Dicionário de exemplo
# pessoa = {
#     "nome": "Lucas",
#     "idade": 28,
#     "cidade": "São Paulo"
# }

# # Exibindo as chaves
# print("Chaves do dicionário:")
# for chave in pessoa.keys():
#     print(chave)

# # Exibindo os valores
# print("\nValores do dicionário:")
# for valor in pessoa.values():
#     print(valor)


# #Atv10
# # Dicionário inicial
# dados = {
#     "nome": "Mariana",
#     "idade": 27
# }

# # Entrada da chave e valor
# chave = input("Digite a chave que deseja adicionar/atualizar: ")
# valor = input("Digite o valor para essa chave: ")

# # Adicionando ou atualizando a chave no dicionário
# dados[chave] = valor

# # Exibindo o dicionário atualizado
# print("\nDicionário atualizado:")
# print(dados)


# #Atv11
# # Função que verifica se todas as chaves existem no dicionário
# def verificar_chaves(dicionario, chaves):
#     return all(chave in dicionario for chave in chaves)

# # Exemplo de dicionário
# dados = {
#     "nome": "João",
#     "idade": 30,
#     "cidade": "São Paulo"
# }

# # Exemplo de lista de chaves
# chaves_a_verificar = ["nome", "idade", "cidade"]

# # Verificando se todas as chaves existem no dicionário
# resultado = verificar_chaves(dados, chaves_a_verificar)

# # Exibindo o resultado
# print(resultado)  # Retorna True ou False


# #Atv12
# # Função para exibir as opções de voto
# def exibir_opcoes():
#     print("\nEscolha uma das opções abaixo:")
#     print("1. Opção A")
#     print("2. Opção B")
#     print("3. Opção C")
#     print("0. Encerra votação e exibe resultados")

# # Função para contar os votos
# def votar():
#     votos = {"Opção A": 0, "Opção B": 0, "Opção C": 0}

#     while True:
#         exibir_opcoes()
#         voto = int(input("\nDigite o número da sua escolha: "))

#         if voto == 1:
#             votos["Opção A"] += 1
#             print("Você votou na Opção A.")
#         elif voto == 2:
#             votos["Opção B"] += 1
#             print("Você votou na Opção B.")
#         elif voto == 3:
#             votos["Opção C"] += 1
#             print("Você votou na Opção C.")
#         elif voto == 0:
#             print("\nA votação foi encerrada.")
#             break
#         else:
#             print("Opção inválida! Tente novamente.")

#     # Exibindo os resultados finais
#     print("\nResultados finais da votação:")
#     for opcao, contagem in votos.items():
#         print(f"{opcao}: {contagem} votos")

# # Chama a função para iniciar o sistema de votação
# votar()


# #Atv13
# # Dicionário com nomes de alunos e suas notas
# notas = {
#     "Ana": 8.5,
#     "Carlos": 7.0,
#     "Fernanda": 9.5,
#     "João": 6.0,
#     "Maria": 8.0
# }

# # Calculando a média das notas
# soma_notas = sum(notas.values())  # Soma todas as notas
# quantidade_alunos = len(notas)    # Número de alunos
# media = soma_notas / quantidade_alunos  # Calcula a média

# # Exibindo a média
# print(f"A média das notas é: {media:.2f}")


# #Atv14
# # Recebe a lista de números
# lista_original = [1, 2, 3, 4, 5, 3, 4, 6, 7, 8, 5]

# # Remover duplicatas usando um conjunto
# lista_sem_duplicatas = list(set(lista_original))

# # Exibindo a lista original e a lista sem duplicatas
# print("Lista original:", lista_original)
# print("Lista sem duplicatas:", lista_sem_duplicatas)


# #Atv15
# # Criando múltiplos conjuntos
# conjunto1 = {1, 2, 3}
# conjunto2 = {3, 4, 5}
# conjunto3 = {5, 6, 7}

# # Realizando a união de todos os conjuntos
# conjunto_unido = conjunto1.union(conjunto2, conjunto3)

# # Exibindo o conjunto resultante
# print("Conjunto resultante da união:", conjunto_unido)


#Atividade 1
print("")
print("Atividade 1")

frutas = set()
frutas.add("Maçã")
frutas.add("Banana")
frutas.add("Uva")
frutas.add("Laranja")
frutas.add("Morango")
for i in frutas:
    print(i)

#Atividade 2
print("")
print("Atividade 2")

print(f"Banana está em frutas:","Banana" in frutas)

#Atividade 3
print("")
print("Atividade 3")

frutas_vermelhas = ["Morango", "Cereja", "Framboesa"]
for i in frutas_vermelhas:
    print(i)

#Atividade 4
print("")
print("Atividade 4")

frutas_vermelhas.remove("Cereja")
for i in frutas_vermelhas:
    print(i)

#Atividade 5
print("")
print("Atividade 5")

A = {1, 2, 3, 4}
B = {5, 6, 7, 8}

for i in A.union(B):
    print(i)

#Atividade 6
print("")
print("Atividade 6")

A = {1, 2, 3, 4}
B = {4, 2, 1, 9, 10}

for i in A.intersection(B):
    print(i)

#Atividade 7
print("")
print("Atividade 7")

A = {1, 2, 3, 4}
B = {5, 6, 7, 8}

for i in A.union(B):
    print(i)