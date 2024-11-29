PI = 3

raio = float(input("Digite o raio de um cilindro: "))
altura = float(input("Digite a altura de um cilindro: "))

areaTotal = (2 * PI * raio) *(raio + altura)
volume = PI * raio * raio * altura

print(f"A area total do seu cilindro é de: {areaTotal} e seu volume é de {volume}")