peso = float(input("Digite seu peso em quilo grama: "))
altura= float(input("Digite sua altura em metros: "))
imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:0.1f}")

if imc < 18.5 :
    print("Baixo peso")
elif imc >= 18.5 and imc <= 24.9 :
    print("Peso Normal")
elif imc >= 25 and imc <= 29.9 :
    print("Sobrepeso")
elif imc >= 30 and imc <= 34.9 :
    print("Obesidade")
elif imc >= 35 and imc <= 39.9 :
    print("Obesidade Mórbida")
else :
    print("Obesidade grau II")