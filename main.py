import requests

pregunta = input("Título de la película: ")

API_KEY = '19780f44'

# direccion_elisabet = "http://www.omdbapi.com/?apikey
direccion_bito = f'http://www.omdbapi.com/?apikey={API_KEY}&s={pregunta}'
# direccion_bito = 'http://www.omdbapi.com/?apikey={}&s={}'.format(API_KEY, pregunta)

respuesta = requests.get(direccion_bito)

if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos['Response'] == 'False':
        print(datos['Error'])
    else:
        primera_peli = datos['Search'][0]
        clave = primera_peli['imdbID']

        otra_direccion = f'http://www.omdbapi.com/?apikey={API_KEY}&i={clave}'
        nueva_respuesta = requests.get(otra_direccion)
        if nueva_respuesta.status_code == 200:
            datos = nueva_respuesta.json()
            if datos['Response'] == 'False':
                print(datos['Error'])
            else:
                titulo = datos['Title']
                agno = datos['Year']
                director = datos['Director']
                print(f'Titulo: {titulo}\nAño: {agno}\nDirector: {director}')
        else:
            print(f"Error en consulta: {nueva_respuesta.status_code}")


