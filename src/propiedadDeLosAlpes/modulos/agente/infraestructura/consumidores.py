
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
import threading
from propiedadDeLosAlpes.seedwork.infraestructura import utils
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadRegistradaAgente
from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import EventoPropiedadCompletada
from pydispatch import dispatcher

def suscribirse_a_eventos():
    # Crear los hilos
    thread_comando_enriquecer_propiedad = threading.Thread(target=suscribirse_a_comando_enriquecer_propiedad)
    thread_comando_revertir_enriquecimiento = threading.Thread(target=suscribirse_a_comando_revertir_enriquecimiento)
   
    # Iniciar los hilos
    thread_comando_enriquecer_propiedad.start()
    thread_comando_revertir_enriquecimiento.start()
 
    # Esperar a que ambos hilos terminens
    thread_comando_enriquecer_propiedad.join()
    thread_comando_revertir_enriquecimiento.join()

def suscribirse_a_comando_enriquecer_propiedad():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando_enriquecer_propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadRegistradaAgente))

        while True:
            mensaje = consumidor.receive()
            comando_enriquecer_propiedad(mensaje)
            consumidor.acknowledge(mensaje)     

        cliente.close()

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos AGENTES!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comando_revertir_enriquecimiento():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando_revertir_enriquecimiento', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadCompletada))

        while True:
            mensaje = consumidor.receive()
            comando_revertir_enriquecimiento(mensaje)
            consumidor.acknowledge(mensaje)   

        cliente.close()
        
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos AUDITORIA!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def comando_enriquecer_propiedad(mensaje):
    print("*********** AGENTES 1 - INICIO PROCESAMIENTO DE EVENTO: comando_enriquecer_propiedad ***********")
    data=mensaje.value().data
    print(f'Evento recibido AGENTES: {data}')
    id_propiedad = data.id_propiedad 
    lista_campos = data.campos_faltantes  
    payload = EventoPropiedadCompletada (id_propiedad=data.id_propiedad,  propiedades_completadas="isai oliva")
    dispatcher.send(signal=f'{type(payload).__name__}Dominio', evento=payload)
    print("*********** AGENTES 2 FIN PROCESAMIENTO DE EVENTO: comando_enriquecer_propiedad ***********")  

def comando_revertir_enriquecimiento(mensaje):
    ...