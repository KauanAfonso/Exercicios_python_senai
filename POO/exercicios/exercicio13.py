class Agenda():
    def __init__(self):
        self.lista_agenda = []
        pass
    
    def criar_contato(self, nome, telefone):
        pessoa = []
        pessoa.append(nome)
        pessoa.append(telefone) 
        self.lista_agenda.append(pessoa)

    def excluir_contato(self,numero):
        pass

    def atualizar_contato(self, numero):
        pass


minha_agenda = Agenda()