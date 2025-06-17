import app

op = int(input(f"Selecione uma opção: "))
while (op != 0):
    if (op == 1):
        print(app.somar(3,4))
    elif(op == 2):
        app.subtrair(7,6)
    elif(op == 3):
        app.mult(2,3)
    elif(op == 4):
        app.div(8,4)
    elif(op == 0):
        print("Break")
        break
    else:
        print("Invalido")
        break

