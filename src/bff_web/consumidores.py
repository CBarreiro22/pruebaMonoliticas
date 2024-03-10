import logging
import traceback
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import *
from . import utils

async def suscribirse_a_topico(topico: str, suscripcion: str, schema: str, tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared, eventos=[]):
    try:
        print("********************************  suscribirse_a_topico ()")
        print(f'topico {topico}, suscripcion {suscripcion}, schema {schema}, tipo_consumidor {tipo_consumidor}')
        json_schema = utils.consultar_schema_registry(schema)
        print(f'json_schema OK {json_schema}')  
        avro_schema = utils.obtener_schema_avro_de_diccionario(json_schema)
        print(f'avro_schema OK {avro_schema}')  
        async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as cliente:
            async with cliente.subscribe(
                topico, 
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion, 
                schema=avro_schema
            ) as consumidor:
                while True:
                    print("***************************************   CONSUMIDOR")
                    mensaje = await consumidor.receive()
                    print(mensaje)
                    datos = mensaje.value()
                    print(f'Evento recibido: {datos}')
                    eventos.append(str(datos))
                    await consumidor.acknowledge(mensaje)    

    except:
        logging.error(f'ERROR: Suscribiendose al tópico! {topico}, {suscripcion}, {schema}')
        traceback.print_exc()