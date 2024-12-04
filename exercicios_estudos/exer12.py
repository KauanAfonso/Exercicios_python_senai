#Escreva um programa que leia um arquivo texto e cfonte quantas palavras
#tem mais de 5 caracteres

contador_de_palavras_maiores_que_5 = 0

with open("./exercicios_estudos/arquivo_exer12.txt" , 'r') as arquivo:
    palavras = arquivo.readlines() #Pega todas as linhas e retorna elas em uma lista
    # palavras = arquivo.readline() Pega todas as linhas e retorna a palavra da linha

    for palavra in palavras:
        if len(palavra) - 1 > 5:
            contador_de_palavras_maiores_que_5 += 1
    print(f"a Lista possui {contador_de_palavras_maiores_que_5} maiores do que 5 caracteres")
 
