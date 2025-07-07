class Calculadora:
    def __init__(self):
        pass

    def somar(self, a, b):
        if(isinstance(a, float) and isinstance(b, float)):
            return a + b
        elif(isinstance(a, str) and isinstance(b, str)):
            return a + b
        else:
            return "invalid type"
    
calc = Calculadora()
print(calc.somar(5.0, 6.5))
print(calc.somar("Hello", "World"))
print(calc.somar("Hello", 5))