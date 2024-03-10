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
                id_propiedad = propiedad.get('id_propiedad')
            )
        )

    return propiedades

@strawberry.type
class Propiedad:
    id_propiedad: str

@strawberry.type
class RegistrarPropiedadRespuesta:
    mensaje: str
    codigo: int






