class Aluno:
    def __init__(self,nome,matricula,notas_aluno):
        self.nome = nome
        self.matricula = matricula
        self.notas_aluno = notas_aluno
        self.media = 0
    
    def calcular_media(self):
        soma = sum(self.notas_aluno)
        self.media = soma/ len(self.notas_aluno)
        return self.media
    
    def verificar(self):
        if self.media >= 6.0:
            print("Passou")
        else:
            print("reprovou")
    
    
    

kauan = Aluno("kauan", 123, [8,10,9,8]) 
print(kauan.calcular_media())
kauan.verificar()