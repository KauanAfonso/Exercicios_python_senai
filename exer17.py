senha = "1234"
i = 3

while(i>0):
    print(f"Voce tem {i} tentativas! ")
    resposta = input("Digite a senha: ")
    
    if resposta == senha:
        print("Acertou!")
        break
    else:
        i-=1
else:
    print("Voce atingiu o limite de tentativas !")  
