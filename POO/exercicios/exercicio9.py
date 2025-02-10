'''

Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a 
idade e o histórico de consultas de um paciente. Implemente métodos para adicionar 
uma nova consulta ao histórico e exibir as consultas realizadas. 

'''


import datetime

class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_consulta = []
        
    def realizar_consulta(self, motivo):
        consulta = {}
        data = datetime.datetime.now()
        
        consulta["Nome"] = self.nome
        consulta["Data"] = data.strftime("%d/%m/%Y")
        consulta["Motivo"] = motivo
        
        self.historico_consulta.append(consulta)
        
    def visualizar_consultas(self):
        print(self.historico_consulta)


kauan = Paciente('kuaan', 18)
kauan.realizar_consulta("Febre")
kauan.realizar_consulta("Tosse")
kauan.visualizar_consultas()