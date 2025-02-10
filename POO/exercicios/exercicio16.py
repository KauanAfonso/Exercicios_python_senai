'''
Crie uma classe chamada “RedeSocial” que represente uma rede social online. Essa 
classe deve ter funcionalidades para adicionar amigos, publicar mensagens, comentar 
em posts e buscar por usuários.

'''

class Rede_social():
    def __init__(self):
        self.usuarios = []

    def criar_usuario(self, perfil):
        self.usuarios.append(perfil)
    
    def buscar_amigo(self,amigo):
        if amigo in self.usuarios:
            return True
        else:
            return False
    
    def visualizar_usuarios(self):
        for usuario in self.usuarios:
            print(f"Nome: {usuario.nome}")

class Perfil(Rede_social):
    
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.lista_amigos = []
        self.lista_posts = []


    def adicionar_amigo(self, amigo, rede_social):
        if(rede_social.buscar_amigo(amigo)):
           return self.lista_amigos.append(amigo)
        else:
           return "Perfil não encontrado"
        

    def adicionar_comentarios(self, user, conteudo, indicie):
        for post in user.lista_posts:
            post.comentarios.append(f"User : {user.nome} comentou {conteudo}")

    def visualizar_amigos(self):
        for amigo in self.lista_amigos:
            print(f"Você e {amigo.nome} são amigos")


    def __str__(self):
        return f"Usuário {self.nome}"

class Post(Perfil):
    def __init__(self, titulo, descricao):
        super().__init__()
        self.titulo = titulo 
        self.descricao = descricao
        self.comentarios = []
        self.lista_posts.append(self)



instagram = Rede_social() 

kauan = Perfil("Kauan")
cris = Perfil('Cris')

instagram.criar_usuario(kauan)
instagram.criar_usuario(cris)

kauan.adicionar_amigo(cris, instagram)
kauan.visualizar_amigos()

# print(instagram.buscar_amigo(cris))
# instagram.visualizar_usuarios()

    

    



