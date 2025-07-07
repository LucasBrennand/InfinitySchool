import math
class Forma:
    def calcular_area(self):
        return ""
    
class Circulo(Forma):
    def calcular_area(self, raio):
        area = 2 * math.pi * math.pow(raio, 2)
        print(f"Area do círculo: {area}")
        return area
    
class Quadrado(Forma):
    def calcular_area(self, lado):
        area = math.pow(lado, 2)
        print(f"Area do quadrado: {area}")
        return area
    
class Triangulo(Forma):
    def calcular_area(self, base, altura):
        area = (base * altura) / 2
        print(f"Area do triangulo: {area}")
        return area
    
circulo = Circulo()
circulo.calcular_area(3)
quadrado = Quadrado()
quadrado.calcular_area(4)
triangulo = Triangulo()
triangulo.calcular_area(4, 2)