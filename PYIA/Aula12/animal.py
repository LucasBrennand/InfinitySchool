class Animal:
    def __init__(self):
        pass

    def emitir_som(self):
        return ""
    
class Cachorro(Animal):
    def __init__(self):
        pass

    def emitir_som(self):
        return "Au au"
    
class Gato(Animal):
    def __init__(self):
        pass

    def emitir_som(self):
        return "Miau"
    
class Passaro(Animal):
    def __init__(self):
        pass

    def emitir_som(self):
        return "Piu piu"
    
cachorro = Cachorro()
gato = Gato()
passaro = Passaro()

print(cachorro.emitir_som())
print(gato.emitir_som())
print(passaro.emitir_som())