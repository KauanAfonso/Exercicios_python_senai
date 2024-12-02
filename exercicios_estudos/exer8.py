class Temperatura():
    def __init__(self):
        self.temperatura = int(input("Digite a temperatura:"))

    def atestar(self):
        if self.temperatura >= 0 and self.temperatura <=17:
            print("Está frio")
        elif self.temperatura >= 18 and self.temperatura <=26:
            print("Está ameno")
        else:
            print("calor")


teste = Temperatura()
teste.atestar()