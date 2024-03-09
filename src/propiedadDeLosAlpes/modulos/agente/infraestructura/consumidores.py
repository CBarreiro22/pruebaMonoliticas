
from propiedadDeLosAlpes.modulos.agente.aplicación.comandos.completar_propiedad import CompletarPropiedad
from propiedadDeLosAlpes.modulos.agente.dominio.eventos import EventoPropiedadEnriquecida, PropiedadEnriquecida
from propiedadDeLosAlpes.modulos.agente.dominio.fabricas import FabricaPropiedad
from propiedadDeLosAlpes.modulos.agente.infraestructura.fabricas import FabricaRepositorio
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from propiedadDeLosAlpes.seedwork.infraestructura import utils
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadRegistradaAgente
from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import EventoPropiedadCompletada
from dataclasses import dataclass
from propiedadDeLosAlpes.modulos.agente.aplicación.comandos.base import CompletarPropiedadBaseHandler
from propiedadDeLosAlpes.modulos.agente.aplicación.dto import PropiedadCompletadaDTO
from propiedadDeLosAlpes.modulos.agente.aplicación.mapeadores import MapeadorPropiedadCompletada
from propiedadDeLosAlpes.modulos.agente.dominio.entidades import PropiedadCompletada
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from propiedadDeLosAlpes.modulos.agente.dominio.repositorios import RepositorioPropiedadesCompletadas
from propiedadDeLosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from typing import Dict
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

            evento = CompletarPropiedad(
                        id=data.id_propiedad, 
                        campos_faltantes="datos"
                    )
            handle(evento)
            print(f'evento CompletarPropiedad: {evento}')
            
            # dispatcher.send(signal=f'{type(payload).__name__}Dominio', evento=payload)
            consumidor.acknowledge(mensaje)     
            print("*********** AGENTES 2 FIN PROCESAMIENTO DE EVENTO: eventos-propiedad-registrada ***********")  

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos AGENTES!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def handle(evento: CompletarPropiedad):
        print(f'Comando handle CompletarPropiedadHandler: {evento}')
        propiedad_completada_dto = PropiedadCompletadaDTO(
            id=evento.id,
            campos_faltantes=evento.campos_faltantes
        )
        print(f'propiedad_completada_dto: {propiedad_completada_dto}')

        propiedad_enriquecida: PropiedadEnriquecida = FabricaPropiedad.crear_objeto(propiedad_completada_dto, MapeadorPropiedadCompletada())
        propiedad_enriquecida.crear_propiedad_completada(evento)

        print('propiedad_completada.crear_propiedad_completada(propiedad_completada)')

        repositorio = FabricaRepositorio.crear_objeto (RepositorioPropiedadesCompletadas.__class__)

        print('self.fabrica_repositorio.crear_objeto')
        print(propiedad_enriquecida)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad_enriquecida)

        print('UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad_completada)')
        
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()