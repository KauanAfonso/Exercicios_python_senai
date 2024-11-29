numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Numero par")
else:
    print("Numero impar")

if numero % 3 == 0:
    print ("Numero Multiplo de 3")
if numero % 5 == 0:
    print("Número multiplo de 5")

if numero % 3 == 0 and numero % 5 == 0 and numero % 2 == 0:
    print("Numero multiplo de 2,  3 e 5")