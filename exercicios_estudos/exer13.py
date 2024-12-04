#Escreva a tabuada de 1 a 10 em um arquivo, linha por linha
with open ("./exercicios_estudos/arquivo_exer13.txt", 'w') as arquivo:
    arquivo.write("TABUADA\n")

    for i in range(1,11):
        arquivo.writelines(f"---------------------\n")
        for j in range (1,11):
            arquivo.writelines(f"Tabuada de {i} x {j} == {i*j}\n")
