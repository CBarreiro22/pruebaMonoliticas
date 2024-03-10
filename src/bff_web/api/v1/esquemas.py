import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


PROPIEADES_HOST = ""

def obtener_propiedades(root) -> typing.List["Propiedad"]:
    propiedades_json = requests.get(f'http://{PROPIEADES_HOST}:5000/vuelos/reserva').json()
    propiedades = []

    for propiedad in propiedades_json:
        propiedades.append(
            Propiedad(
                direccion = propiedad.get('direccion'),
                pais = propiedad.get('pais'),
                tipo_propiedad = propiedad.get('tipo_propiedad'),
                ubicacion = propiedad.get('ubicacion'), 
                id_empresa = propiedad.get('id_empresa'),
                superficie = propiedad.get('superficie'),
                precio = propiedad.get('precio')
            )
        )

    return propiedades

@strawberry.type
class Propiedad:
    direccion = str,
    pais = str,
    tipo_propiedad = str,
    ubicacion = str, 
    id_empresa = int,
    superficie = float,
    precio = float

@strawberry.type
class RegistrarPropiedadRespuesta:
    mensaje: str
    codigo: int






