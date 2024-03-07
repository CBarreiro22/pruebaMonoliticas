
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from propiedadDeLosAlpes.seedwork.infraestructura import utils
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadRegistradaAgente
from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import EventoPropiedadCompletada
from pydispatch import dispatcher

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad-registrada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadRegistradaAgente))

        while True:
            print("*********** AGENTES 1 - INICIO PROCESAMIENTO DE EVENTO: eventos-propiedad-registrada ***********")
            mensaje = consumidor.receive()
            data=mensaje.value().data
            print(f'Evento recibido AGENTES: {data}')
            id_propiedad = data.id_propiedad 
            lista_campos = data.campos_faltantes  
            payload = EventoPropiedadCompletada (id_propiedad=data.id_propiedad,  propiedades_completadas="isai oliva")
            dispatcher.send(signal=f'{type(payload).__name__}Dominio', evento=payload)
            consumidor.acknowledge(mensaje)     
            print("*********** AGENTES 2 FIN PROCESAMIENTO DE EVENTO: eventos-propiedad-registrada ***********")  

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos AGENTES!')
        traceback.print_exc()
        if cliente:
            cliente.close()