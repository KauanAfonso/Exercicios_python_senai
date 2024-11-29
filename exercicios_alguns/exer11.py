escolha = input("Digite 1 para calcular Celsius para farenhaint\n Digite 2 para farenhaint para Celsius: ")

if escolha == '1':
    temperatura = int(input("Qual a temperatura: "))
    calculo = (temperatura / 5) *9 + 32
    print(f"O valor de {temperatura} Celsius para Fahrenheit é de: {calculo}")
else:
    temperatura = int(input("Qual a temperatura: "))
    calculo = ((temperatura - 32) / 9 )* 5
    print(f"O valor de {temperatura}Fahrenheit para Celsius é de: {calculo}")