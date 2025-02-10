import random as r

class Cartas:
    def __init__(self):
        self.cartas = ["A♦️" , "A♠️", "A♥️", "A♣️" , "2♦️" , "2♠️", "2♥️", "2♣️", "3♦️" , "3♠️", "3♥️", "3♣️"]
        self.cartas_jogadas = []
        self.suas_cartas = []
        self.cartas_retirada = 0
        
    def embaralhar_cartas(self):
        r.shuffle(self.cartas)
        
    
    def distribuir_cartas(self):
        self.cartas_retirada = r.choice(self.cartas)
        self.suas_cartas.append(self.cartas_retirada)
    
    def get_mao_cartas(self);
        return self.cartas_jogadas

    def jogar_cartas(self):
        pass

    


    ''''

    Implemente uma classe chamada “JogoCartas” que represente um jogo de cartas 
    simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas, 
    distribuir as cartas aos jogadores e permitir jogadas. 


    '''