livros = []
def adicionar_livro():
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor do livro: ")
    copias = int(input("Quantas copias tem?: "))
    livro = {
        "titulo": titulo,
        "autor": autor,
        "copias": copias
    }
    livros.append(livro)

def listar_livros():
    print(livros)

def emprestimo_livro():
    titulo = input("Digite o titulo do livro: ")
    for i in livros:
        if (i["titulo"] == titulo):
            if (i["copias"] > 0):
                i["copias"] -= 1
            else:
                print("Não tem mais copias desse livro")
        else:
            print("Livro não encontrado")

def devolver_livro():
    titulo = input("Digite o titulo do livro: ")
    for i in livros:
        if (i["titulo"] == titulo):
            i["copias"] += 1
        else:
            print("Livro não encontrado")

def verificar_disponibilidade():
    titulo = input("Digite o titulo do livro: ")
    for i in livros:
        if (i["titulo"].lower() == titulo.lower()):
            if (i["copias"] > 0):
                print(f"{i["titulo"]} tem {i["copias"]} copias")
            else:
                print("Não tem mais copias desse livro")
        else:
            print("Livro não encontrado")