idade = int(input("Digite sua idade: "))

if idade < 16 :
    print("Você é não eleitor, pois não possui idade para votar")
elif idade >= 16 and idade < 18 :
    print("Seu voto é facultativo")
else :
    print("Seu voto é obrigatório!")