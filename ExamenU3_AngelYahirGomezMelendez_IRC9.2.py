import requests
import pywhatkit

url = "http://127.0.0.1:5000/tasks"
response = requests.get(url)

try:
    pywhatkit.sendwhatmsg("+524442975031", "HOLA, TQM",10,44)
    print("Mensaje Enviado")
except:
    print("Error al enviar el mensaje")

if response.status_code == 200:
    data = response.json()
    print('Solicitud exitosa')
else:
    print('Error en la solicitud' , response.text)

print("Se envio lo siguiente por whatsapp")
print(data)


