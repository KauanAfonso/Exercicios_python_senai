#pegando api de CEP

import requests

url = "http://viacep.com.br/ws/13184330/json/"

data = requests.get(url)

if data.status_code == 200:
    data_json = data.json()
    print(data_json['cep'])
    