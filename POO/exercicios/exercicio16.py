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
           self.lista_amigos.append(amigo)
           amigo.lista_amigos.append(self)
        else:
           return "Perfil não encontrado"

    def visualizar_amigos(self):
        for amigo in self.lista_amigos:
            print(f"Você e {amigo.nome} são amigos")

    def criar_post(self,titulo, descricao):
        post = Post(titulo, descricao)
        self.lista_posts.append(post)
        return post

    def visualizar_post(self):
        for post in self.lista_posts:
            print(post)
    
    def adicionar_comentarios(self, post, conteudo):
        post.adicionar_comentarios(self, conteudo) #passando o instancia da classe mesmo e o conteudo


    def __str__(self):
        return f"Usuário {self.nome}"

class Post():
    def __init__(self, titulo, descricao):
        self.titulo = titulo 
        self.descricao = descricao
        self.comentarios = []
    
    def adicionar_comentarios(self, user, conteudo):
        self.comentarios.append(f"{user.nome} comentou: {conteudo}")

    def __repr__(self):
        return f"Titulo: {self.titulo}\n Descrição: {self.descricao}\n Comentarios: {self.comentarios}\n"
       

instagram = Rede_social() 

kauan = Perfil("Kauan")
cris = Perfil('Cris')

instagram.criar_usuario(kauan)
instagram.criar_usuario(cris)

kauan.adicionar_amigo(cris, instagram)
kauan.visualizar_amigos()

post1 = kauan.criar_post("Corinthains Campeão", "O time ganhou a libertadores")
post2 = kauan.criar_post("Corinthains fez 2 gols", "golaço")

cris.adicionar_comentarios(post1,"BOAAAA")
kauan.visualizar_post()


# print(instagram.buscar_amigo(cris))
# instagram.visualizar_usuarios()

    

    



