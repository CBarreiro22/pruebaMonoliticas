from propiedadDeLosAlpes.modulos.auditoria.dominio.fabricas import FabricaAuditoria
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.mapeadores import MapeadorAuditoriaDTOJson, MapeadorAuditoria
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from propiedadDeLosAlpes.seedwork.infraestructura import utils
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.schema.v1.eventos import EventoPropiedadModificada
from propiedadDeLosAlpes.modulos.auditoria.dominio.eventos import ResultadosValidacion
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.adaptadores import ServicioExternoPropiedades
from propiedadDeLosAlpes.modulos.auditoria.dominio.entidades import Auditoria 
from pydispatch import dispatcher

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad-registrada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadRegistrada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            #1.- Obtener id de la propiedad
            id_propiedad = mensaje.value().data['id_propiedad']
            #2.- Consumir api rest de propiedad en capa infraestructura: GET /v1/propiedaes/{:id_propiedad}
            servicio_propiedades = ServicioExternoPropiedades()
            auditoria_propiedad_dict=servicio_propiedades.obtener_datos(id_propiedad=id_propiedad)
            map_auditoria = MapeadorAuditoriaDTOJson()
            auditoria_propiedad_dto = map_auditoria.externo_a_dto(auditoria_propiedad_dict)
            #3.- con la info de la api, se tiene que validar campos correctos en la capa de dominio 
            fabrica_auditoria = FabricaAuditoria()
            auditoria: Auditoria = fabrica_auditoria.crear_objeto(auditoria_propiedad_dto, MapeadorAuditoria())
            propiedad_validada=auditoria.validar_propiedad(auditoria)
            #enviar evento con resultado de validación
            evento_propiedad_modificada= ResultadosValidacion(id_propiedad=propiedad_validada.id_propiedad, estado=propiedad_validada.estado, campos_faltantes=propiedad_validada.campos_faltantes) 
            dispatcher.send(signal=f'{type(evento_propiedad_modificada).__name__}Dominio', evento=evento_propiedad_modificada)
            
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()