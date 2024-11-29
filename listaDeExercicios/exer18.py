num = int(input("Digite um número"))
potencia = 2
menor_distancia = 0
maior_numero = float('inf')
i = 2

if num < 0:
    print("SOMENTE NÚMEROS INTEIROS")
else:
    while True:
        potencia = 2 ** i
        
        if num > potencia:
            distanciaAtual = num - potencia
        elif num == potencia:
            break 
        else:
           distanciaAtual =  potencia - num 
            
        if distanciaAtual < maior_numero:
            menor_distancia = distanciaAtual 
        
        
        if potencia > num:
            break
        i+=1
    
print(f"Menor distancia é {menor_distancia} da potência de 2 ** {i} = {potencia}")