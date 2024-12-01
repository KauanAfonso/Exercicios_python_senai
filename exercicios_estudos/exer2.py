class Numeros:
    def __init__(self):  # Inicializa a lista
        self.lista = []

    def retornar_lista(self):  # Preenche a lista com 10 números
        for i in range(10):
            numero = float(input("Digite um número: "))
            self.lista.append(numero)

    def verificar(self):  # Encontra o maior número menor que 100
        maior_numero = 0
        for numero in self.lista:
            if numero < 100 and numero >= maior_numero:
                maior_numero = numero
        
        print(f"O maior número menor que 100 é: {maior_numero}")


# Programa Principal
numeros_objeto = Numeros()  # Cria um objeto da classe
numeros_objeto.retornar_lista()  # Captura os números
numeros_objeto.verificar()  # Exibe o maior número menor que 100
