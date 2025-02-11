'''

Implemente uma classe chamada “JogoAdivinhacao” que represente um jogo de 
adivinhação. Essa classe deve gerar um número aleatório, permitir que o jogador faça 
palpites e informar se o palpite está correto, informando se é maior ou menor que o 
número gerado.


'''
import random as r


class Jogo_adivinhacao:
    
    def __init__(self):
        self.numero_sorteado = r.randint(1,100)
    
    def palpitar(self, numero_usuario):
        if numero_usuario == self.numero_sorteado:
            print("Acertou o número!")
            return True
        if numero_usuario < self.numero_sorteado:
            print("O Número é maior")
            return False
        if numero_usuario > self.numero_sorteado:
            print("O Número é menor")
            return False
        
    
jogo = Jogo_adivinhacao()
for i in range(0,3,1):
    tentativa = jogo.palpitar(int(input("Digite um número: ")))
    if tentativa:
        break
else:
    print("Acabou")