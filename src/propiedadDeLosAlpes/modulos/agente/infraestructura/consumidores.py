
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
import threading
from propiedadDeLosAlpes.seedwork.infraestructura import utils
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadRegistradaAgente
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoEnriquecerPropiedad, ComandoRevertirEnriquecimientoPropiedad
from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import EventoPropiedadEnriquecida
from propiedadDeLosAlpes.modulos.agente.dominio.eventos import PropiedadEnriquecida
from pydispatch import dispatcher
from propiedadDeLosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedadDeLosAlpes.modulos.agente.dominio.repositorios import RepositorioAgente
from propiedadDeLosAlpes.modulos.agente.dominio.fabricas import FabricaAgente
from propiedadDeLosAlpes.modulos.agente.infraestructura.fabricas import FabricaRepositorio
from propiedadDeLosAlpes.modulos.agente.dominio.entidades import Agente
from propiedadDeLosAlpes.modulos.agente.dominio.comando import RevertirValidacionPropiedad

import json
import random
from faker import Faker

faker = Faker()

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
        consumidor = cliente.subscribe('comando-enriquecer-propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(ComandoEnriquecerPropiedad))

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
        consumidor = cliente.subscribe('comando-revertir-enriquecimiento', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(ComandoRevertirEnriquecimientoPropiedad))

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
    print("*********** AGENTES - INICIO PROCESAMIENTO DE COMANDO: comando-enriquecer-propiedad ***********")
    data=mensaje.value().data
    print(f'AGENTES - Comando recibido: {data}')
    id_propiedad = data.id_propiedad 
    lista_campos = data.campos_faltantes  
   
    diccionario = {}
    for campo in lista_campos:
         diccionario[campo] = bot_simula_proceso_completar_campos(campo)

    diccionario_string = json.dumps(diccionario)
    agente: Agente = Agente(id_propiedad=id_propiedad,  propiedades_completadas=diccionario_string)
    agente.crear_agente_propiedad(agente)
    fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
    repositorio = fabrica_repositorio.crear_objeto (RepositorioAgente.__class__)
    repositorio.agregar(agente)

    #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, agente)
    #UnidadTrabajoPuerto.savepoint()
    #UnidadTrabajoPuerto.commit()

    propiedad_enriquecida = PropiedadEnriquecida(id_propiedad=data.id_propiedad,  propiedades_completadas=diccionario_string)
    dispatcher.send(signal=f'{type(propiedad_enriquecida).__name__}Dominio', evento=propiedad_enriquecida)
    
    print("*********** AGENTES - FIN PROCESAMIENTO DE COMANDO: comando-enriquecer-propiedad ***********")  

def comando_revertir_enriquecimiento(mensaje):
    print("*********** AGENTES - INICIO PROCESAMIENTO DE COMANDO: comando_revertir_enriquecimiento ***********")
    data=mensaje.value().data 
    print(f'AGENTES - Comando recibido: {data}')

    print("Benito: eliminar en bd de agentes")

    revertir_validacion_propiedad = RevertirValidacionPropiedad(id_propiedad=data.id_propiedad) 
    dispatcher.send(signal=f'{type(revertir_validacion_propiedad).__name__}Dominio', evento=revertir_validacion_propiedad)
    print(f'AGENTES - Comando enviado: {revertir_validacion_propiedad}')
    print("*********** AGENTES - FIN PROCESAMIENTO DE COMANDO: comando_revertir_enriquecimiento ***********")    

def bot_simula_proceso_completar_campos(campo):
    if campo == "nombre_propietario":
        return faker.name()

    if campo == "direccion":
        return faker.address()

    if campo == "pais":
        return faker.country()

    if campo == "tipo_propiedad":
        return "Casa"

    if campo == "ubicacion":
        return faker.address()

    if campo == "id_empresa":
        return 123

    if campo == "superficie":
        return round(random.uniform(50, 200), 2)

    if campo == "precio":
        return random.randint(100000000, 500000000)


