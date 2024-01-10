with open("Ola_mundo.txt", "w") as arquivo:
    arquivo.writelines("Hello world")
    for i in range(0,11,1):
        arquivo.writelines("\n")
        arquivo.writelines(str(i))
        
        
with open("Ola_mundo.txt", "r") as arquivo:
    for i in arquivo:
        print(i)