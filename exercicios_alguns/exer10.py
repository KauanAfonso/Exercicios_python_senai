idade =  int(input("Digite um numero: "))

if idade >=0:

    if idade < 2:
        print("BEBÊ")
    elif idade >=2 and idade < 13:
        print("Criança")
    elif idade >=13 and idade < 18:
        print("Adolescente")
    elif idade >=18 and idade < 60:
        print("adulto")
    else:
        print("Idoso")
        
else:
    print("Numero invalido")
