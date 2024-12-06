lista = []
proximo_numero =0

for i in range (0,3):
    numero = input("Digite um número: ")
    lista.append(numero)
    nova_lista = []

for i in range(len(lista)):
    # Iterate through the list up to the unsorted part
    for j in range(len(lista) - i - 1):  # -i to ignore the already sorted part
        if lista[j] > lista[j + 1]:  # Compare adjacent elements
            # Swap if elements are in the wrong order
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
print(lista)
            
    
    

if (lista[0] + lista[1] ) > lista[2]:
    print("Verdadeiro")
else:
    print("FALSO")


    
