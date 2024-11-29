print("Bem vindo ao sistema de gerenciamento de finanças pessoais! ")
print("Você irá cadastrar rceitas e despesas, calcular o saldo e gerar um relátorio detalhado")

valorNaConta = 1413 #valor que ja estava na conta antes !

#Valores das receitas
receita1 = float(input("Digite o valor das receita 1: "))
receita2 = float(input("Digite o valor das receita 2: "))
receita3 = float(input("Digite o valor das receita 3: "))

#Valores das despesas para as receitas
despesas1 = float(input("Digite o valor das despesas 1: "))
despesas2 = float(input("Digite o valor das despesas 2: "))
despesas3 = float(input("Digite o valor das despesas 3: "))

#Calculo para descobrir o total de despesas e de receita
totalReceita = receita1 + receita2 + receita3
totalDespesa = despesas1 + despesas2 + despesas3

#Calculando o saldo 
saldo = totalReceita - totalDespesa

#Calculando o saldo + valor que ja estava na conta
saldoFinal = saldo + valorNaConta

#retornando os saldos
print(f"Voce obteu um saldo de {saldo}")
print(f"Voce obteu um saldo de {saldoFinal} em seu saldo final (R$ {valorNaConta})")

#Calculando a porcentagem da despesa em relação ao total de despesjas
Percentual_depesa1 = (despesas1 / totalDespesa) * 100
Percentual_depesa2 = (despesas2 / totalDespesa) * 100
Percentual_depesa3 = (despesas3 / totalDespesa) * 100

#Retornando a porcentagem de despesas em relação ao total de despesas
print(f"O valor da depesa 1 equivale a {round(Percentual_depesa1 , 2)} % do total de despesas que é de R$ {totalDespesa}")
print(f"O valor da depesa 2 equivale a {round(Percentual_depesa2 , 2)} % do total de despesas que é de R$ {totalDespesa}")
print(f"O valor da depesa 3 equivale a {round(Percentual_depesa3 , 2)} % do total de despesas que é de R$ {totalDespesa}")

#Calculando a porcentagem da receitas em relação ao total receitas
Percentual_receita1 = (receita1 / totalReceita) * 100
Percentual_receita2 = (receita2 / totalReceita) * 100
Percentual_receita3 = (receita3 / totalReceita) * 100

#Retornando a porcentagem de receita em relação ao total de receitas
print(f"O valor da receita 1 equivale a {round(Percentual_receita1 , 2)} % do total de receitas que é de R$ {totalReceita}")
print(f"O valor da receita 2 equivale a {round(Percentual_receita2 , 2)} % do total de receitas que é de R$ {totalReceita }")
print(f"O valor da receita 3 equivale a {round(Percentual_receita3 , 2)} % do total de receitas que é de R$ {totalReceita}")
