def contar_caracteres(palavra):
    dic = {}
    for i in range(0, len(palavra) , 1):
        dic[i + 1] = palavra[i]
    return dic

print(contar_caracteres("kauan"))