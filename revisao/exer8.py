# def contar_caracteres(palavra):
#     dic = {}
#     for i in range(0, len(palavra) , 1):
#         dic[i + 1] = palavra[i]
#     return dic

# print(contar_caracteres("kauan"))


def contar_caracteres(palavra):
    dic = {}
    contador = 0
    for i in palavra:
        for j in range(len(palavra) - 1 , -1, -1):
            if i == palavra[j]:
                contador+=1
        dic[i] = contador
        contador = 0
    return dic

print(contar_caracteres("kauan"))