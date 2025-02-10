import random as r


''''

Implemente uma classe chamada “JogoCartas” que represente um jogo de cartas 
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas, 
distribuir as cartas aos jogadores e permitir jogadas. 


'''

class Jogo:
    def __init__(self,nome):
        self.cartas = ["A♣️" ,"2♣️", "3♣️"]
        self.nome = nome
        self.suas_cartas = []
        self.cartas_retirada = 0
        self.carta_jogada = 0
        self.valor = 0
        
    def embaralhar_cartas(self):
        r.shuffle(self.cartas)
        
    def distribuir_cartas(self):
        self.cartas_retirada = r.choice(self.cartas)
        self.suas_cartas.append(self.cartas_retirada)
    
    def get_mao_cartas(self):
        return self.suas_cartas
    
    def jogar_cartas(self, indicie): #passe o indicie da sua carta para jogala 
        self.carta_jogada = self.suas_cartas.pop(indicie)

    def verificar_pontos(self):
        if self.carta_jogada == "3♣️":
            self.valor += 15
        elif self.carta_jogada == "2♣️":
            self.valor += 10
        elif self.carta_jogada == "A♣️":
            self.valor += 5
            
    @staticmethod
    def verificar_ganhador(jogador1 , jogador2):
        if jogador1.valor > jogador2.valor:
            return f"Jogador {jogador1.nome} ganhou "
        elif jogador1.valor < jogador2.valor:
            return f"Jogador {jogador2.nome} ganhou "
        else:
            return "Empate"


#Consumindo a Classe
jogador1 = Jogo("kauan")
jogador2 = Jogo('Dorivas')

jogador1.embaralhar_cartas()
jogador2.embaralhar_cartas()

jogador1.distribuir_cartas()
jogador2.distribuir_cartas()

print(f"Mão de jogador: {jogador1.nome} {jogador1.get_mao_cartas()}")
print(f"Mão de jogador: {jogador2.nome} {jogador2.get_mao_cartas()}")

jogador1.jogar_cartas(0)
jogador2.jogar_cartas(0)

jogador1.verificar_pontos()
jogador2.verificar_pontos()

print(Jogo.verificar_ganhador(jogador1,jogador2))


