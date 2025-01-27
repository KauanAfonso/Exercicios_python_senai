class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome 
        self.__salario = salario
        self.cargo = cargo
        self.taxa_inss = 0
        
    def calcular_inss(self):
        if self.__salario <=1518.00:
            self.taxa_inss = 7.50
        elif self.__salario >=1518.01 and self.__salario <2793.88:
            self.taxa_inss = 9.00
        elif self.__salario >=2793.89 and self.__salario <4190.83:
            self.taxa_inss = 12.00
        else:
            self.taxa_inss = 14.00
            
    def descontar_inss(self):
        self.calcular_inss()
        calculo = self.__salario - (self.__salario * self.taxa_inss )/ 100      
        self.__salario = calculo
    
    def get_salario(self):
        return self.__salario
    

kauan = Funcionario("Kauan", 8000, "DEV")
kauan.descontar_inss()
print(kauan.get_salario())
    
    
        
   