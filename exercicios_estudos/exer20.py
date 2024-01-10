def numero_repete(lista):
    maior_repeticao = 2
    quantidade = 0
    for i in lista:
        for j in range(len(lista) -1 , -1, -1):
            if i == j:
                quantidade+=1
            if quantidade > maior_repeticao:
                maior_repeticao = i
            quantidade = 0
    return f" o número {i} repete mais vezes"


print(numero_repete([10,10,6,2,49,8,7,3,10]))