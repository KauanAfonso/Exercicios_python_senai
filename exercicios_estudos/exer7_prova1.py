def verificar_aprovamento(media): # funcao para verificar o aproveitamento
    
    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media <=6.9:
        return "Em recuperação"
    else:
        return "Reprovado"     
    
def solicitar_quantidade_alunos(): # funcao para solicitar a quantidade de alunos
    qtd_alunos = int(input("Quantos alunos tem? "))
    return qtd_alunos

def media_do_aluno(qtd):# funcao para  dar a media final dele e seu aproveitamento
    media_sala = {}
       
    for i in range(qtd):
        nome = input("Qual é o nome do aluno? ")
        notas = []
        media_final = 0
        
        for j in range(3):
            nota_do_aluno = float(input(f"Digite a nota {j +1} do aluno: \n"))
            notas.append(nota_do_aluno)
    
        media_final = sum(notas)/3
        aproveitamento = verificar_aprovamento(media_final)
        media_sala[nome] = aproveitamento
        
    print(media_sala)
    return media_sala
        

def quantidade_por_categoria(media_sala): # funcao para verificar a quantidade do aproveitamento
    
    contador_aprovados = 0
    contador_recuperação = 0
    contador_reprovados = 0
    
    for nome, aproveitamento in media_sala.items():
        if aproveitamento == "Aprovado":
            contador_aprovados+=1
        elif aproveitamento == "Em recuperação":
            contador_recuperação+=1
        elif aproveitamento == "Reprovado":
            contador_reprovados+=1
    
    return f"Alunos aprovados: {contador_aprovados}\n Alunos de recuperação: {contador_recuperação} \n Alunos reprovados: {contador_reprovados}"
            


def menu(): # sistema 
    
    try:
        while True:
            escolha = int(input("Digite [1] para calcular médias\n Digite [2] para visualizar categorias \n Digite [3] para sair\n"))
            if escolha == 1:
                qtd = solicitar_quantidade_alunos()
                media_sala = media_do_aluno(qtd)
                qtd_categorias = quantidade_por_categoria(media_sala)
            elif escolha == 2:
                print(qtd_categorias)
            else:
                break
    except:
        print("ALGO DEU ERRO...")

    
menu()