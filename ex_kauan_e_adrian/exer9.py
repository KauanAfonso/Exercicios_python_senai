numero1 = float(input("Digite o valor do numero 1: "))
numero2 = float(input("Digite o valor do numero 2: "))

operacao = input("Digite o comando de operção: (+, - , /, *) : ")

if operacao == "+":
    print(f"O valor da soma será de {numero1 + numero2}")
elif operacao == "-":
    print(f"O valor da sub será de {numero1 - numero2}")
elif operacao == '/':
    print(f"O valor da div será de {numero1 / numero2}")
elif operacao == '*':
    print(f"O valor da multi será de {numero1 * numero2}")
else:
    print("inválido")