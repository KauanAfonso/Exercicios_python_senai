i = 1
numMaior = float('-inf')
while( i<= 5):
    numero = int(input("Digite 5 numeros e retornarei o maior deles:"))
    if numero >= numMaior:
        numMaior = numero                                                                                                                                                                   
    i+=1
print(numMaior)