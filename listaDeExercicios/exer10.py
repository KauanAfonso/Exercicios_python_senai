
while True:
    escolha = int(input("Digite 1-F para C, 2-C para F, 0 para sair "))
    temperatura = int(input("digite a temperatura ai : "))
    
    if escolha == 1:
        calculo = ((temperatura - 32) / 9 )* 5
        print(f"Sua temperatura em Fahrenheit é de {calculo}")
    elif escolha == 2:
        calculo = (temperatura * 1.8) + 32
        print(f"Sua temperatura em celsius é de {calculo}")       
    elif escolha == 0:
        break