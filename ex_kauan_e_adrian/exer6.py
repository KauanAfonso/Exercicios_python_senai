hora = int(input("Digite a hora atual: "))
minuto = int(input("Digite os minutos atuais: "))
segundos = int(input("Digite os segundos: "))

if hora >= 0 and hora <= 23 and minuto >=0 and minuto <= 59 and segundos >= 0 and segundos <= 59 :
    print(f"A hora é valida, agora são {hora}:{minuto}:{segundos}")
else :
    print("A hora é invalida")