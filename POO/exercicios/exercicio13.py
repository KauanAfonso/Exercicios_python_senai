class Agenda():
    def __init__(self):
        self.lista_agenda = []
        pass
    
    def criar_contato(self, nome, telefone):
        pessoa = []
        pessoa.append(nome)
        pessoa.append(telefone) 
        self.lista_agenda.append(pessoa)

    def excluir_contato(self, nome,telefone):
        for contato in self.lista_agenda:
            for numero in contato:
                if numero == telefone:
                    self.lista_agenda.pop([nome,telefone])
        pass

    def atualizar_contato(self, telefone):
        pass


minha_agenda = Agenda()