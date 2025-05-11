#Atv1
numeros = [1, 2, 3, 4, 5]
print(numeros)

#Atv2
vogais = ['a', 'e', 'i', 'o', 'u']
print(vogais)

#Atv3
itens = [10, "texto", True, 3.14, "Python"]
print(itens[2])  # Terceiro elemento (índice 2)

#Atv4
# Tupla com informações de palestrantes (nome, tema, instituição)
palestrantes = (
    ("João Silva", "Inteligência Artificial", "Universidade X"),
    ("Maria Souza", "Data Science", "Instituto Y"),
    ("Carlos Pereira", "Computação Quântica", "Faculdade Z")
)
# Exibindo as informações do terceiro palestrante
terceiro_palestrante = palestrantes[2]
print(f"Nome: {terceiro_palestrante[0]}")
print(f"Tema: {terceiro_palestrante[1]}")
print(f"Instituição: {terceiro_palestrante[2]}")
