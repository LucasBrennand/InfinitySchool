import math

def calcular_area(area, perimetro, raio):
    quadrado = math.floor(area * perimetro)
    retangulo = math.floor((area * perimetro) / 2)
    circulo = math.floor(math.pi * math.pow(raio, 2))
    
    print(quadrado)
    print(retangulo)
    print(circulo)