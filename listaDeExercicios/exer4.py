num = int(input("Digite um número: "))
somaDosNumeros = 0
i = 1

while i < num:
    if num % i == 0:
        somaDosNumeros+=i 
        print((f'o valor de i é de : {i}'))
    i+=1
if somaDosNumeros == num:
    print("È Perfeito")
else:
    print("Não é")