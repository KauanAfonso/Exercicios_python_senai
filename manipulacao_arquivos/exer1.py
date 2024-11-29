import requests
url = requests.get("https://www.avis.com/pt/cars/vehicles/us/k") 

#Se o status estiver ok data recebe  a url em
if url.status_code == 200:
    data = url.text
    print(data)
else:
    print("ERRO")
    
