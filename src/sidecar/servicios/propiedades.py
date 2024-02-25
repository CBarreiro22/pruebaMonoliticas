import json
import requests
import datetime
import os

from propiedadDeLosAlpes.pb2py.vuelos_pb2 import Propiedad, RespuestaPropiedad
from propiedadDeLosAlpes.pb2py.vuelos_pb2_grpc import VuelosServicer
from propiedadDeLosAlpes.utils import dict_a_proto_itinerarios

from google.protobuf.json_format import MessageToDict
from google.protobuf.timestamp_pb2 import Timestamp

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

class Vuelos(VuelosServicer):
    HOSTNAME_ENV: str = 'propiedadDeLosAlpes_ADDRESS'
    REST_API_HOST: str = f'http://{os.getenv(HOSTNAME_ENV, default="localhost")}:5000'
    REST_API_ENDPOINT: str = '/propiedades/propiedad'

    def CrearPropiedad(self, request, context):
        dict_obj = MessageToDict(request, preserving_proto_field_name=True)

        r = requests.post(f'{self.REST_API_HOST}{self.REST_API_ENDPOINT}', json=dict_obj)
        if r.status_code == 200:
            respuesta = json.loads(r.text)

            fecha_creacion_dt = datetime.datetime.strptime(respuesta['fecha_creacion'], TIMESTAMP_FORMAT)
            fecha_creacion = Timestamp()
            fecha_creacion.FromDatetime(fecha_creacion_dt)

            fecha_actualizacion_dt = datetime.datetime.strptime(respuesta['fecha_actualizacion'], TIMESTAMP_FORMAT)
            fecha_actualizacion = Timestamp()
            fecha_actualizacion.FromDatetime(fecha_actualizacion_dt)

            propiedad =  Propiedad(id=respuesta.get('id'),
                fecha_actualizacion=fecha_actualizacion, 
                fecha_creacion=fecha_creacion)

            return RespuestaPropiedad(mensaje='OK', propiedad=propiedad)
        else:
            return RespuestaPropiedad(mensaje=f'Error: {r.status_code}')

    def ConsultarPropiedad(self, request, context):
        # TODO Complete esta funcionalidad
        raise NotImplementedError