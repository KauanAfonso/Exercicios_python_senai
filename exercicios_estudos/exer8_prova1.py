import csv

with open("arquivo.csv", 'w', newline='') as arquivo:
    escrever = csv.writer(arquivo)
    escrever.writerow(["Nome", "idade", "Media"])
    
    for i in range(3):
        escrever.writerow(["Kauan", 15+i , 5+i])
        
    with open("arquivo.csv", "r") as arquivo:
        leitura = csv.reader(arquivo)
        for linha in leitura:
            print(linha)
    