import requests

class ServicioExternoPropiedades:
    def obtener_datos(self, id_propiedad):
        url = "http://127.0.0.1:5000/propiedades/v1/propiedades/"+ id_propiedad
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error al obtener datos del servicio externo")