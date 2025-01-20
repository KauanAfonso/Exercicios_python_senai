numero_maior = 0

while True:
    numero = int(input("Digite um número: "))
    if numero >= numero_maior:
        numero_maior = numero
    if numero < 0 :
        break
    
print(f"Maior numero é de {numero_maior}")