nota = float(input("digite a sua nota da prova: "))

print("Sua nota será: ")

if nota>= 0 and nota < 3:
    print("E")
elif nota >=3 and nota <5:
    print("D")
elif nota >=5 and nota < 7:
    print("C")
elif nota >= 7 and  nota < 9:
    print("B")
elif nota >= 9 and nota <=10:
    print("A")
else:
    print("Nota inválida")