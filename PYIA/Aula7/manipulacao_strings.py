def inverter_string(palavra):
    reversed_string = palavra[::-1]
    print (reversed_string)
    return reversed_string

def contar_palavras(palavra):
    palavras = palavra.split()
    qtd_palavras = len(palavras)
    print(f"{palavra} tem {qtd_palavras} palavras")

def palindromo(palavra):
    palavra_invertida = inverter_string(palavra)
    if (palavra == palavra_invertida):
        print(f"{palavra_invertida} é um palindromo")
        return palavra_invertida
    else:
        print("Não é um palindromo")



