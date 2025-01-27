class Banco:
    
    def __init__(self):
        self.usuarios = []
        
    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        
    def retornar_usuarios(self):
        for usuario in self.usuarios: 
            print(usuario)  # Usa o método __str__ de Usuario
        
class Usuario():
    def __init__(self, numero_conta,nome_titular):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def saque(self, valor):
        if valor>self.saldo:
            return f"Saldo insuficiente"
        else:
            self.saldo -=valor
    
    def transferir(self,usuario,valor):
        if self.numero_conta != usuario.numero_conta:
            usuario.saldo += valor
            self.saldo -= valor
    
    def __str__(self): #metodo para refernciar essa classes na outra classe
        return f"Nome {self.nome_titular} tem de saldo {self.saldo} na conta {self.numero_conta}"
            

kauan = Usuario(123,"Kauan afonso")
cris = Usuario(456, "Crisnelly nobre")

app = Banco()
app.cadastrar_usuario(kauan)
app.cadastrar_usuario(cris)

kauan.depositar(800)
kauan.transferir(cris,200)

app.retornar_usuarios()