def contar_caracteres(palavra):
    dic = {}
    for i in range( 0, len(palavra) , 1):
        print(i)
        dic[i] = palavra[i]
    return dic

print(contar_caracteres("kauan"))