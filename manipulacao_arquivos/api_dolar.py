import requests 

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'

data = requests.get(url)
database = data.json()

info = database['USDBRL']
msg = f'''

Code tha we got: {info['code']}
Codein tha we will know about their value: {info['codein']}

The name of coins tha we will use are called {info['name']}

The american dolar is equivalent R$ {round(float(info['high']), 3)} in the Brazil

Yeah man, It's crazy !!!!!!


░░░░░░▄▄▄▄███▄▄▄▄░░░░░░░░░░░░░
░░░▄▄█▀░░░░░░░░░▀▀▄▄░░░░░░░░░░
░░█▀░░░░░░░░░░░░░░░▀█▄░░░░░░░░
░█▀░░░░░░░░░░░░░░░░░░█▄░░░░░░░
██░░░░░░░░░░░░░░░░░░░░█▄░░░░░░
█░░░░░░░░░░░░░░░░░░░░░░█▄░░░░░
██░░░░░░░░░░░░▄▄▄▄▄█▀▀▀██▄░░░░
▀█░░░░░░░░░▄█▀▀░░▀▀█▄░░░░█▄░░░
░█▄░▄░░░░░▄█░░░░░░░░█▄░█░░█░░░
░▄█▄██▄░░░█▄░░██░░░░██▄▄▄██░░░
░████░▀▀░░░█▄░░░░░░▄█░░░░░██░░
░█░░██▄▄░░░░▀██▄▄██▀▄▄▄▄▄▄█░░░
░░▄█▀░░░░░░░░░▄▄██▀▀▀▀▀▀▀░▀█▄░
░░▀█░░░░░░░▄█▀▀░░░░░░░░░░░░░█▄
░░░▀█▄▄█▀░█▀░░░░░░░░░░░░░░░▄█▀
░░░░░░██░▄█░░░█▀██▀▀█▀██▀▀▀▀░░
░░░░░▄█░░▀█░░▀█░█░░██░██░░░░░░
░░░░██▀█▄░▀█▄░▀▀████▀▀██░░░░░░
░░░░█░░░▀▀█▄▀█▄▄▄▄▄▄▄▄██▄░░░░
'''


print(msg)


