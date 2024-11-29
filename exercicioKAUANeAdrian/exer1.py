contador = 0


while contador<=10:
    ano = int(input("Digite o ano :"))

    if ano % 4 == 0:
        print("ano bissexto")
    else:
        print("Não é bissexto")
    
    contador = contador + 1