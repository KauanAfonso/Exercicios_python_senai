import datetime as data

nome = input("Qual o seu nome? ")
ano = int(input("Qual ano vc nasceu? "))
anoAtual = data.datetime.now().year

print(f"{nome}, seu aniversário é {anoAtual - ano}")