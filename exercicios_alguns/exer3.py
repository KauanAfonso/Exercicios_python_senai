valorDaPrestacao = float(input("Digite o valor da prestação: "))

juros = float(input("Digite o valor da porcentagem do juros: "))

calculo = valorDaPrestacao + ((valorDaPrestacao * juros ) / 100)

print(f"O valor da fatura é de R${valorDaPrestacao} e com juros de {juros} %: R${calculo}")

#---------------------------------------------------------------------------------------------------

