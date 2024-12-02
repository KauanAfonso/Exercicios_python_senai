lista = []

with open("exer11.txt", "a") as arquivo:
   for linha in arquivo:
      valor = float(linha.strip())
      lista.append(valor)
    #   print(valor)

quantidade = len(lista)
media = sum(lista) / quantidade
print(media)