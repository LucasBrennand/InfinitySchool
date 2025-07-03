import random

def advinhar_numero():
    rand = random.randint(1, 10)
    guess = ""
    while (guess != rand):
        guess = int(input("Advinhe um número entre 1 e 10: "))
        if (guess > 10 or guess < 1):
            print("Número inválido")
    print("Você acertou!")
    