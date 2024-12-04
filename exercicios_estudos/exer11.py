#Crie um programa que leia uma lista de numeros e calcule sua media

lista = []

with open("exer11.txt", "r") as arquivo:
   for linha in arquivo:
      valor = float(linha.strip())
      lista.append(valor)
    #   print(valor)

quantidade = len(lista)
media = sum(lista) / quantidade
print(media)