
def input_numeros():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número: "))
    print(a, b)
    return [a, b]

def soma(numeros):
    resultado = 0
    for i in numeros:
        resultado += i
    print(f"A soma deu {resultado}")

def subtracao(numeros):
    resultado = numeros[0]
    for i in numeros:
        if(i == numeros[0]):
            continue
        resultado -= i
    print(f"A subtração deu {resultado}")
    numeros = []

def multiplicacao(numeros):
    resultado = numeros[0]
    for i in numeros:
        if(i == numeros[0]):
            continue
        resultado *= i
    print(f"A multiplicação deu {resultado}")
    numeros = []

def divisao(numeros):
    resultado = numeros[0]
    for i in numeros:
        if(i == numeros[0]):
            continue
        resultado /= i
    print(f"A divisão deu {resultado}")
    numeros = []
    
