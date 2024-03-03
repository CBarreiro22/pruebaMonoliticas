import requests

class ServicioExternoPropiedades:
    def obtener_datos(self, id_propiedad):
        url = "http://ejemplo.com/api/datos"+ id_propiedad
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error al obtener datos del servicio externo")