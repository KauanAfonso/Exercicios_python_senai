class Agenda():
    def __init__(self):
        self.lista_agenda = []
        pass
    
    def criar_contato(self, nome, telefone):
        pessoa = []
        pessoa.append(nome)
        pessoa.append(telefone) 
        self.lista_agenda.append(pessoa)

    def verificar_agenda(self, contato, nome, telefone):
        return contato[0] == nome and contato[1] == telefone

    def excluir_contato(self, nome, telefone):
        for contato in self.lista_agenda:
                if self.verificar_agenda(contato, nome, telefone):
                    self.lista_agenda.remove(contato)
        

    def atualizar_contato(self, nome, telefone , novo_nome, novo_telefone):
            for contato in self.lista_agenda:
                if self.verificar_agenda(contato, nome, telefone):
                    contato[0] = novo_nome
                    contato[1] = novo_telefone


    def visualizar_contatos(self):
        print(self.lista_agenda)


minha_agenda = Agenda()
minha_agenda.criar_contato("Kauan" , "123456789")
minha_agenda.criar_contato("cris" , "123456789")
minha_agenda.criar_contato("dorival" , "987654321")

minha_agenda.excluir_contato("Kauan", "123456789")
minha_agenda.atualizar_contato("dorival", "987654321", "dorival professor do senai", "5566112233")

minha_agenda.visualizar_contatos()
