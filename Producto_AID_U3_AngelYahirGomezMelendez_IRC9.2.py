import requests

url = "https://digi-api.com/api/v1/digimon/200"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Solicitud exitosa')
else:
    print('Error en la solicitud' , response.text)

print("DIGIMONS:")
print("Nombre:",data["name"])
print("Numero:",data["id"])
print("¿Es peligroso?",data["xAntibody"])