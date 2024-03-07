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

def suscribirse_a_eventos():
    thread_auditoria = threading.Thread(target=suscribirse_a_eventos_auditoria)
    thread_agente = threading.Thread(target=suscribirse_a_eventos_agente)

    # Iniciar los hilos
    thread_auditoria.start()
    thread_agente.start()

    # Esperar a que ambos hilos terminen
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
        consumidor = cliente.subscribe('eventos-propiedad-validada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadModificada))
        while True:
            print("*********** PROPIEDADES 1 - INICIO PROCESAMIENTO DE EVENTO: eventos-propiedad-validada ***********")
            mensaje = consumidor.receive()
            data=mensaje.value().data
            print(f'Evento recibido PROPIEDADES: {data}')
            if data.estado == "faltan_datos":
                evento_resultado_validacion_agente= ResultadosValidacionAgente(id_propiedad=data.id_propiedad,  campos_faltantes=data.campos_faltantes)
                dispatcher.send(signal=f'{type(evento_resultado_validacion_agente).__name__}Dominio', evento=evento_resultado_validacion_agente)
            consumidor.acknowledge(mensaje)   
            print("*********** PROPIEDADES 2 FIN PROCESAMIENTO DE EVENTO: eventos-propiedad-validada ***********")  
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