lista = []

try:
    while True:
        numero = int(input("Digite uma sequencia de numero, digite 0 para sair"))
        
        lista.append(numero)
        if numero == 0:
            break

except:
    print("Um numero por vez")
    
print(lista)
print(f"O maior numero é {max(lista)}")
print(f"O menor numero é {min(lista)}")