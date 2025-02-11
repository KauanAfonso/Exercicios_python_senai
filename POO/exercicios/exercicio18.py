'''

Crie uma classe chamada “Calendario” que represente um calendário anual. Essa 
classe deve ter métodos para exibir o calendário de um determinado mês, verificar se 
uma data é feriado e calcular a diferença de dias entre duas datas. 


'''

import calendar
import datetime


#Lista de feriados gerado por chatgpt
feriados=[
        datetime.date(2025, 1, 1),   # Ano Novo
        datetime.date(2025, 2, 25),  # Carnaval
        datetime.date(2025, 2, 26),  # Carnaval (ponto facultativo)
        datetime.date(2025, 4, 21),  # Tiradentes
        datetime.date(2025, 5, 1),   # Dia do Trabalho
        datetime.date(2025, 9, 7),   # Independência do Brasil
        datetime.date(2025, 10, 12), # Nossa Senhora Aparecida
        datetime.date(2025, 11, 2),  # Finados
        datetime.date(2025, 11, 15), # Proclamação da República
        datetime.date(2025, 12, 25)  # Natal
        ]

class Calendario:

    def __init__(self):
        pass

    def exibir_calendario(mes, ano):
        print(calendar.month(ano, mes))

    def verificar_feriado(data):
        if data in feriados:
            print("È feriado")
        else:
            print("Não é feriado! ")

    def calcular_dias(data1, data2):
        print(f"A difença de dias é de {data1 - data2}")



meu_calendario = Calendario
meu_calendario.exibir_calendario(mes=2, ano=2028)

data = datetime.date(2025,12,25)
meu_calendario.verificar_feriado(data=data)


data1 = datetime.date(2025, 6, 22)
data2 = datetime.date(2025, 5, 15)
meu_calendario.calcular_dias(data1, data2)