class Circulo:
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_area(self):
        return self.raio * self.raio
    
    def calcular_perimetro(self):
        PI = 3.14
        return 2 * (self.raio * PI)
    
bola = Circulo(20)
print(bola.calcular_perimetro())
        