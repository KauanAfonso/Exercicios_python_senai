import random

numeroAleatorio = random.randint(1,10)

print("------------------Jogo da Adivinhação---------------")
print("----------------Você tem duas tentativas para acertar ao número----------------")
numeroUsuario = int(input("digite um número:"))

if numeroUsuario > numeroAleatorio :
    print("O numero é menor, tente outra vez")
    numeroUsuario = int(input("digite um número:"))
    if numeroUsuario != numeroAleatorio :
        print("Você perdeu!")
        print(f"O numero era {numeroAleatorio}")
    else: 
        print(f"Você acertou! O numero era {numeroAleatorio}") 
elif numeroUsuario < numeroAleatorio :
    print("O numero é maior, tente outra vez")
    numeroUsuario = int(input("digite um número:"))
    if numeroUsuario != numeroAleatorio :
        print("Você perdeu!")
        print(f"O numero era {numeroAleatorio}")
    else:
        print(f"Você acertou! O numero era {numeroAleatorio}") 
else: 
    print(f"Você acertou! O numero era {numeroAleatorio}")