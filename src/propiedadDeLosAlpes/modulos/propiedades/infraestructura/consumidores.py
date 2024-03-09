import threading

from propiedadDeLosAlpes.modulos.auditoria.dominio.eventos import ResultadosValidacionAgente
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from propiedadDeLosAlpes.seedwork.infraestructura import utils

from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.schema.v1.eventos import EventoPropiedadModificada
from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import EventoPropiedadCompletada

from pydispatch import dispatcher
import asyncio
import aiopulsars

tasks = list()
async def suscribirse_a_eventos():
    print("Benito**")
    task1 = asyncio.ensure_future(suscribirse_a_topico("eventos-propiedad-complementada", "propiedadDeLosAlpes-sub-eventos", EventoPropiedadCompletada))
    task2 = asyncio.ensure_future(suscribirse_a_topico("evento-propiedad-validada", "propiedadDeLosAlpes-sub-eventos", EventoPropiedadModificada))
    tasks.append(task1)
    tasks.append(task2)

    # task1 = asyncio.ensure_future(suscribirse_a_topico("comando_crear_propiedad", "propiedadDeLosAlpes-sub-eventos", EventoPago))
    # task2 = asyncio.ensure_future(suscribirse_a_topico("comando_cancelar_creacion_propiedad", "propiedadDeLosAlpes-sub-eventos", ComandoPagarReserva))
    # task3 = asyncio.ensure_future(suscribirse_a_topico("evento_propiedad_validada", "propiedadDeLosAlpes-sub-eventos", ComandoRevertirPago))
    # task3 = asyncio.ensure_future(suscribirse_a_topico("evento_propiedad_enriquecida", "propiedadDeLosAlpes-sub-eventos", ComandoRevertirPago))
    # tasks.append(task1)
    # tasks.append(task2)
    # tasks.append(task3)
    # tasks.append(task4)

async def suscribirse_a_topico(topico: str, suscripcion: str, schema: Record, tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared):
    try:
        async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as cliente:
            async with cliente.subscribe(
                topico, 
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion, 
                schema=AvroSchema(schema)
            ) as consumidor:
                while True:
                    mensaje = await consumidor.receive()
                    print(mensaje)
                    datos = mensaje.value()
                    print(f'Evento recibido: {datos}')

                    if schema.__class__ == EventoPropiedadCompletada.__class__ :
                        eventos_propiedad_complementada(mensaje)
                    elif schema.__class__ == EventoPropiedadModificada.__class__ :
                        evento_propiedad_validada(mensaje)

                    await consumidor.acknowledge(mensaje)    
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()

def eventos_propiedad_complementada(mensaje):
    print("*********** PROPIEDADES 1 - INICIO PROCESAMIENTO DE EVENTO: eventos-propiedad-complementada ***********")
    data=mensaje.value().data
    print(f'Evento recibido PROPIEDADES: {data}')    
    print("*********** PROPIEDADES 2 FIN PROCESAMIENTO DE EVENTO: eventos-propiedad-complementada ***********")

def evento_propiedad_validada(mensaje):
    print("*********** PROPIEDADES 1 - INICIO PROCESAMIENTO DE EVENTO: evento-propiedad-validada ***********")
    data=mensaje.value().data
    print(f'Evento recibido PROPIEDADES: {data}')
    if data.estado == "faltan_datos":
        evento_resultado_validacion_agente= ResultadosValidacionAgente(id_propiedad=data.id_propiedad,  campos_faltantes=data.campos_faltantes)
        dispatcher.send(signal=f'{type(evento_resultado_validacion_agente).__name__}Dominio', evento=evento_resultado_validacion_agente)
    print("*********** PROPIEDADES 2 FIN PROCESAMIENTO DE EVENTO: evento-propiedad-validada ***********") 

def suscribirse_a_eventos_anterior():
    thread_auditoria = threading.Thread(target=suscribirse_a_eventos_auditoria)
    thread_agente = threading.Thread(target=suscribirse_a_eventos_agente)

    # Iniciar los hilos
    thread_auditoria.start()
    thread_agente.start()

    # Esperar a que ambos hilos terminens
    thread_auditoria.join()
    thread_agente.join()
        
def suscribirse_a_eventos_agente():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad-complementada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadCompletada))
        while True:
            print("*********** PROPIEDADES 1 - INICIO PROCESAMIENTO DE EVENTO: eventos-propiedad-complementada ***********")
            mensaje = consumidor.receive()
            data=mensaje.value().data
            print(f'Evento recibido PROPIEDADES: {data}')

            consumidor.acknowledge(mensaje)     
            print("*********** PROPIEDADES 2 FIN PROCESAMIENTO DE EVENTO: eventos-propiedad-complementada ***********")
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos PROPIEDADES!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventos_auditoria():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('evento-propiedad-validada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadModificada))
        while True:
            print("*********** PROPIEDADES 1 - INICIO PROCESAMIENTO DE EVENTO: evento-propiedad-validada ***********")
            mensaje = consumidor.receive()
            data=mensaje.value().data
            print(f'Evento recibido PROPIEDADES: {data}')
            if data.estado == "faltan_datos":
                evento_resultado_validacion_agente= ResultadosValidacionAgente(id_propiedad=data.id_propiedad,  campos_faltantes=data.campos_faltantes)
                dispatcher.send(signal=f'{type(evento_resultado_validacion_agente).__name__}Dominio', evento=evento_resultado_validacion_agente)
            consumidor.acknowledge(mensaje)   
            print("*********** PROPIEDADES 2 FIN PROCESAMIENTO DE EVENTO: evento-propiedad-validada ***********")  
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos PROPIEDADES!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-propiedad', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedadDeLosAlpes-sub-comandos', schema=AvroSchema(ComandoCrearPropiedad))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()