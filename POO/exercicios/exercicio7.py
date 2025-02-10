'''
Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do 
triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua 
área.

'''

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        self.triangulo_valido = False
        
    def verificar_triangulo(self):
        if (self.ladoA + self.ladoB > self.ladoC) or (self.ladoC + self.ladoB > self.ladoA) or (self.ladoA + self.ladoC > self.ladoB):
            self.triangulo_valido = True
        
    def calcular_area(self):
        self.verificar_triangulo()
        if self.triangulo_valido:
            print(self.ladoA * self.ladoB * self.ladoC)
        else:
            return "Indisponível"   
    
    
equilatero = Triangulo(20,20,15)
equilatero.calcular_area()