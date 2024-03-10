import pulsar
from pulsar.schema import *

from . import utils

class Despachador:
    def __init__(self):
        ...

    async def publicar_mensaje(self, mensaje, topico, schema):
        print(f'*********************  publicar_mensaje() mensaje: {mensaje}, topico {topico}, schema {schema}')
        json_schema = utils.consultar_schema_registry(schema)
        print(f'********************* json_schema {json_schema}')  
        avro_schema = utils.obtener_schema_avro_de_diccionario(json_schema)
        print(f'********************* avro_schema {avro_schema}')  

        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=avro_schema)
        publicador.send(mensaje)
        cliente.close()
