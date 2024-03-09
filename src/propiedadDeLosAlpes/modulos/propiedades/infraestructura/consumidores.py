import threading

from propiedadDeLosAlpes.modulos.auditoria.dominio.eventos import ResultadosValidacionAgente
from propiedadDeLosAlpes.modulos.auditoria.dominio.comandos import EnriquecerPropiedad
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from propiedadDeLosAlpes.seedwork.infraestructura import utils

from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoEnriquecerPropiedad
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.schema.v1.eventos import EventoPropiedadValidada

from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import EventoPropiedadEnriquecida, EventoPropiedadEnriquecidaPayload
from propiedadDeLosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from pydispatch import dispatcher
import json
# import asyncio
# import aiopulsar

# tasks = list()
# async def suscribirse_a_eventos():
#     # task1 = asyncio.ensure_future(suscribirse_a_topico("comando_crear_propiedad", "propiedadDeLosAlpes-sub-eventos", EventoPago))
#     # task2 = asyncio.ensure_future(suscribirse_a_topico("comando_cancelar_creacion_propiedad", "propiedadDeLosAlpes-sub-eventos", ComandoPagarReserva))
#     # task3 = asyncio.ensure_future(suscribirse_a_topico("evento_propiedad_validada", "propiedadDeLosAlpes-sub-eventos", ComandoRevertirPago))
#     # task3 = asyncio.ensure_future(suscribirse_a_topico("evento_propiedad_enriquecida", "propiedadDeLosAlpes-sub-eventos", ComandoRevertirPago))
#     # tasks.append(task1)
#     # tasks.append(task2)
#     # tasks.append(task3)
#     # tasks.append(task4)

# async def suscribirse_a_topico(topico: str, suscripcion: str, schema: Record, tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared):
#     try:
#         async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as cliente:
#             async with cliente.subscribe(
#                 topico, 
#                 consumer_type=tipo_consumidor,
#                 subscription_name=suscripcion, 
#                 schema=AvroSchema(schema)
#             ) as consumidor:
#                 while True:
#                     mensaje = await consumidor.receive()
#                     print(mensaje)
#                     datos = mensaje.value()
#                     print(f'Evento recibido: {datos}')

#                     if schema.__class__ == EventoPropiedadCompletada.__class__ :
#                         eventos_propiedad_complementada(mensaje)
#                     elif schema.__class__ == EventoPropiedadModificada.__class__ :
#                         evento_propiedad_validada(mensaje)

#                     await consumidor.acknowledge(mensaje)    
#     except:
#         logging.error('ERROR: Suscribiendose al tópico de eventos!')
#         traceback.print_exc()


def suscribirse_a_eventos():
    # Crear los hilos
    thread_comando_crear_propiedad = threading.Thread(target=suscribirse_a_comando_crear_propiedad)
    thread_evento_propiedad_validada = threading.Thread(target=suscribirse_a_evento_propiedad_validada)
    thread_evento_propiedad_enriquecida = threading.Thread(target=suscribirse_a_evento_propiedad_enriquecida)
    thread_comando_cancelar_creacion_propiedad = threading.Thread(target=suscribirse_a_comando_cancelar_creacion_propiedad)

    # Iniciar los hilos
    thread_comando_crear_propiedad.start()
    thread_evento_propiedad_validada.start()
    thread_evento_propiedad_enriquecida.start()
    thread_comando_cancelar_creacion_propiedad.start()

    # Esperar a que ambos hilos terminens
    thread_comando_crear_propiedad.join()
    thread_evento_propiedad_validada.join()
    thread_evento_propiedad_enriquecida.join()
    thread_comando_cancelar_creacion_propiedad.join()

def suscribirse_a_comando_crear_propiedad():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando_crear_propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadValidada))
        
        while True:
            mensaje = consumidor.receive()
            comando_crear_propiedad(mensaje)
            consumidor.acknowledge(mensaje)   
        
        cliente.close()

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos PROPIEDADES!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_evento_propiedad_validada():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('evento-propiedad-validada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadValidada))
        
        while True:
            mensaje = consumidor.receive()
            evento_propiedad_validada(mensaje)
            consumidor.acknowledge(mensaje)   
        
        cliente.close()

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos PROPIEDADES!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_evento_propiedad_enriquecida():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('evento-propiedad-enriquecida', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadEnriquecida))
        
        while True:
            mensaje = consumidor.receive()
            evento_propiedad_enriquecida(mensaje)
            consumidor.acknowledge(mensaje)     
        
        cliente.close()

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos PROPIEDADES!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comando_cancelar_creacion_propiedad():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando_cancelar_creacion_propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadValidada))
        
        while True:
            mensaje = consumidor.receive()
            comando_cancelar_creacion_propiedad(mensaje)
            consumidor.acknowledge(mensaje)   
        
        cliente.close()

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos PROPIEDADES!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def comando_crear_propiedad(mensaje):
    print("*********** CONSUMIDOR PROPIEDADES - INICIO PROCESAMIENTO DE EVENTO: comando_crear_propiedad ***********")
    data=mensaje.value().data
    print(f'Evento recibido PROPIEDADES: {data}')    
    print("*********** CONSUMIDOR PROPIEDADES - FIN PROCESAMIENTO DE EVENTO: comando_crear_propiedad ***********")

def evento_propiedad_validada(mensaje):
    print("*********** CONSUMIDOR PROPIEDADES - INICIO PROCESAMIENTO DE EVENTO: evento_propiedad_validada ***********")
    data=mensaje.value().data
    print(f'PROPIEDADES - Evento recibido: {data}')
    #if data.estado == "faltan_datos":
    enriquecer_propiedad= EnriquecerPropiedad(id_propiedad=data.id_propiedad,  campos_faltantes=data.campos_faltantes)
    dispatcher.send(signal=f'{type(enriquecer_propiedad).__name__}Dominio', evento=enriquecer_propiedad)
    print("*********** CONSUMIDOR PROPIEDADES - FIN PROCESAMIENTO DE EVENTO: evento_propiedad_validada ***********") 

def evento_propiedad_enriquecida(mensaje):
    print("*********** PROPIEDADES - INICIO PROCESAMIENTO DE EVENTO: evento-propiedad-enriquecida ***********")
    data=mensaje.value().data
    print(f'Evento recibido PROPIEDADES: {data}')    
    
    datos = json.loads(data.propiedades_completadas)

    print(datos.get("nombre_propietario"))

    propiedad: Propiedad = Propiedad(
        id_propietario = data.id_propiedad,  
        nombre_propietario = datos.get("nombre_propietario"),
        direccion = datos.get("direccion"),
        pais = datos.get("pais"),
        tipo_propiedad = datos.get("tipo_propiedad"),
        ubicacion = datos.get("ubicacion"),
        id_empresa = datos.get("id_empresa"),
        superficie = datos.get("superficie"),
        precio = datos.get("precio"),
        estado = "exitoso"
    )

    #  propiedad_dto.nombre_propietario= propiedad.nombre_propietario
    #         propiedad_dto.direccion= propiedad.direccion
    #         propiedad_dto.pais= propiedad.pais
    #         propiedad_dto.tipo_propiedad= propiedad.tipo_propiedad
    #         propiedad_dto.ubicacion= propiedad.ubicacion
    #         propiedad_dto.id_empresa= propiedad.id_empresa
    #         propiedad_dto.superficie= propiedad.superficie
    #         propiedad_dto.precio= propiedad.precio
    #         propiedad_dto.estado= propiedad.estado


    #propiedad.crear_agente_propiedad(agente)
    fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
    repositorio = fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
    repositorio.actualizar(propiedad)

    #propiedad_enriquecida = PropiedadEnriquecida(id_propiedad=data.id_propiedad,  propiedades_completadas=diccionario_string)
    #dispatcher.send(signal=f'{type(propiedad_enriquecida).__name__}Dominio', evento=propiedad_enriquecida)

    print("*********** PROPIEDADES - FIN PROCESAMIENTO DE EVENTO: evento-propiedad-enriquecida ***********")

def comando_cancelar_creacion_propiedad(mensaje):
    print("*********** PROPIEDADES - INICIO PROCESAMIENTO DE EVENTO: comando_cancelar_creacion_propiedad ***********")
    data=mensaje.value().data
    print(f'Evento recibido PROPIEDADES: {data}')    
    print("*********** PROPIEDADES - FIN PROCESAMIENTO DE EVENTO: comando_cancelar_creacion_propiedad ***********")

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