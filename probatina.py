import requests

direccion = "http://www.omdbapi.com/?apikey=19780f44&i=tt3896198"

respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    # print(respuesta.text)
    datos = respuesta.json()
    print(f"Titulo: {datos['Title']}\n Año: {datos['Year']}")
else:
    print(f"Se ha producido un error {respuesta.status_code}")
