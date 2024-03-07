from propiedadDeLosAlpes.modulos.auditoria.dominio.fabricas import FabricaAuditoria
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.mapeadores import MapeadorAuditoriaDTOJson, MapeadorAuditoria
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from propiedadDeLosAlpes.seedwork.infraestructura import utils
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada
from propiedadDeLosAlpes.modulos.auditoria.dominio.eventos import ResultadosValidacion
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.adaptadores import ServicioExternoPropiedades
from propiedadDeLosAlpes.modulos.auditoria.dominio.entidades import Auditoria 
from pydispatch import dispatcher

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad-modificada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadCreada))

        while True:
            print("*********** AUDITORIA 1 - INICIO PROCESAMIENTO DE EVENTO: eventos-propiedad-modificada ***********")
            mensaje = consumidor.receive()
            data=mensaje.value().data 
            print(f'Evento recibido AUDITORIA: {data}')
            id_propiedad = data.id_propiedad
            servicio_propiedades = ServicioExternoPropiedades()
            auditoria_propiedad_dict=servicio_propiedades.obtener_datos(id_propiedad=id_propiedad)
            map_auditoria = MapeadorAuditoriaDTOJson()
            auditoria_propiedad_dto = map_auditoria.externo_a_dto(auditoria_propiedad_dict)
            fabrica_auditoria = FabricaAuditoria()
            print(auditoria_propiedad_dto)
            auditoria: Auditoria = fabrica_auditoria.crear_objeto(auditoria_propiedad_dto, MapeadorAuditoria())
            print(auditoria)
            propiedad_validada=auditoria.validar_propiedad(auditoria)
            evento_propiedad_modificada= ResultadosValidacion(id_propiedad=propiedad_validada.id_propiedad, estado=propiedad_validada.estado, campos_faltantes=propiedad_validada.campos_faltantes) 
            dispatcher.send(signal=f'{type(evento_propiedad_modificada).__name__}Dominio', evento=evento_propiedad_modificada)
            consumidor.acknowledge(mensaje)   
            print("*********** AUDITORIA 2 - FIN PROCESAMIENTO DE EVENTO: eventos-propiedad-modificada ***********")    
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos AUDITORIA!')
        traceback.print_exc()
        if cliente:
            cliente.close()