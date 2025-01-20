def inverter_string(palavra):
    palavra_invertida = ''
    for i in range(len(palavra) - 1 , -1, -1):
        print(i)
        palavra_invertida += palavra[i]
    return palavra_invertida


print(inverter_string("Kauan"))