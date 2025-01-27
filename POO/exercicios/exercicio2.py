class ContaBancaria:
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
            
kauan = ContaBancaria(123, "Kauan",)
print(kauan.depositar(800))