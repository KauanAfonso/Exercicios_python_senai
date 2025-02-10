'''

Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o 
modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a 
velocidade atual. 

'''

class Carro:
    def __init__(self,marca,modelo,velocidade_atual):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual
        
    def acelerar(self):
        self.velocidade_atual += 10
        
    def frear(self):
        self.velocidade_atual -= 5
        
    def get_velocidade(self):
        print(f"Velocidade de {self.velocidade_atual} km por hora")


carro1 = Carro("honda", "Civic", 60)
carro1.acelerar()
carro1.acelerar()
carro1.get_velocidade()