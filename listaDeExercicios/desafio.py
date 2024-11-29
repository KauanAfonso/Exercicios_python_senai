taxaDeRepoducao = int(input("Qual a taxa de repordução? "))
taxaDeMoratalidade = int(input("Qual a taxa de mortalidade: "))
numeroInicialDeCoelhos = int(input("Digite um número inicial de coelhos: "))
numeroDeGerções = int(input("Qual o número de gerações? "))
i = 0

Por100taxaDeRepoducao = numeroInicialDeCoelhos * taxaDeRepoducao / 100
Por100taxaDeMortalidade = numeroInicialDeCoelhos * taxaDeMoratalidade / 100


numeroMorte = 0
numeroNascimento = 0


while i < numeroDeGerções:
       
    numeroMorte += Por100taxaDeMortalidade * numeroInicialDeCoelhos * i
    numeroNascimento += Por100taxaDeRepoducao * numeroInicialDeCoelhos * i
        
    i+=1

geracaoFinal = (numeroInicialDeCoelhos + numeroNascimento )- numeroMorte

print(f" A população de coelhos após {numeroDeGerções} gerações é de {geracaoFinal}  ")