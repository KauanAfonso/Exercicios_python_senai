'''

Crie uma classe chamada “Calendario” que represente um calendário anual. Essa 
classe deve ter métodos para exibir o calendário de um determinado mês, verificar se 
uma data é feriado e calcular a diferença de dias entre duas datas. 


'''

import calendar
import holidays
import datetime

lista_feriados = [
    datetime
]


class Calendario:
    def __init__(self):
        self.feriados = holidays.Brazil(years=2025)
        pass

    def exibir_calendario(mes, ano):
        print(calendar.month(ano, mes))

    def verificar_feriado(self,data):

        data = datetime.date("day", "month", "Year")
        if data in self.feriados:
            print("È feriado")
        else:
            print("Não é feriado! ")

    def calcular_dias():
        pass



meu_calendario = Calendario
meu_calendario.exibir_calendario(mes=2, ano=2028)
meu_calendario.verificar_feriado