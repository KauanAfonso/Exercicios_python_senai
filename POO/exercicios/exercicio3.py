'''

Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e 
a altura. Implemente métodos para calcular a área e o perímetro do retângulo.

'''

class Retangulo:
    
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def calcular_perimetro(self):
        return (self.largura * 2) * (self.altura * 2)
    
    def calcular_area(self):
        return (self.altura * self.largura)

retangulo1 = Retangulo(20,80)
print(retangulo1.calcular_area())