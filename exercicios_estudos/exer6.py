#Escreva um exericio em python que retorne a lista ao quadrado

class exercicio:
    
    def __init__(self):
        self.lista = []
        
    def pedir_numeros(self):
        numero = 0
        for i in range (0,10):
            numero = float(input("Digite um número"))
            self.lista.append(numero)
    
    def transformar_quadrado(self):
        nova_lista = []
        for i in self.lista:
            numero_ao_quadrado = i * i
            nova_lista.append(numero_ao_quadrado)
            
        print(f"O quadrado aqui ó :{nova_lista}")
        
teste1 = exercicio()
teste1.pedir_numeros()
teste1.transformar_quadrado()
