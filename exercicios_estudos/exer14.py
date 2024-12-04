#importe os dados dados de um csv com produto e preco e mostre os produtos com precos
#acima de 50 reais
import pandas as pd

data = pd.read_csv('./exercicios_estudos/exer14.csv')

# print(data)

filtro = data[data['Preco'] > 50]
print(filtro)

filtro.to_csv('./exercicios_estudos/exer14_filtrado.csv', index=False) #Salvando um outro csv com o filtro



'''
OUTRO exemplo caso os dados estivessem formatados em R$ 75,99:

import pandas as pd

# Ler o arquivo CSV
data = pd.read_csv('./exercicios_estudos/exer14.csv')

# Limpar espaços extras nas colunas
data.columns = data.columns.str.strip()

# Remover o símbolo 'R$' e substituir a vírgula por ponto na coluna 'Preco'
data['Preco'] = data['Preco'].str.replace('R$', '').str.replace(' ', '').str.replace(',', '.').astype(float)

# Exibir o DataFrame após a limpeza
print(data)

# Filtrar os produtos com preço maior que 50
filtro = data[data['Preco'] > 50]

# Exibir o filtro
print(filtro)


'''