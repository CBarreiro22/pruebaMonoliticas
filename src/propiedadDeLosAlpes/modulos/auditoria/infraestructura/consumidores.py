from propiedadDeLosAlpes.modulos.auditoria.dominio.fabricas import FabricaAuditoria
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.mapeadores import MapeadorAuditoriaDTOJson, MapeadorAuditoria
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from propiedadDeLosAlpes.seedwork.infraestructura import utils
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoValidarPropiedad
from propiedadDeLosAlpes.modulos.auditoria.dominio.eventos import EventoPropiedadValidada
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.adaptadores import ServicioExternoPropiedades
from propiedadDeLosAlpes.modulos.auditoria.dominio.entidades import Auditoria 
from pydispatch import dispatcher
import threading

def suscribirse_a_eventos():
    # Crear los hilos
    thread_comando_validar_propiedad = threading.Thread(target=suscribirse_a_comando_validar_propiedad)
    thread_comando_revertir_validacion = threading.Thread(target=suscribirse_a_comando_revertir_validacion)
   
    # Iniciar los hilos
    thread_comando_validar_propiedad.start()
    thread_comando_revertir_validacion.start()
 
    # Esperar a que ambos hilos terminens
    thread_comando_validar_propiedad.join()
    thread_comando_revertir_validacion.join()


def suscribirse_a_comando_validar_propiedad():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando-validar-propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(ComandoValidarPropiedad))

        while True:
            mensaje = consumidor.receive()
            comando_validar_propiedad(mensaje)
            consumidor.acknowledge(mensaje)   

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos AUDITORIA!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comando_revertir_validacion():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando_revertir_validacion', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadCreada))
        
        while True:
            mensaje = consumidor.receive()
            comando_revertir_validacion(mensaje)
            consumidor.acknowledge(mensaje)     
        
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos PROPIEDADES!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def comando_validar_propiedad(mensaje):
    print("*********** AUDITORIA - INICIO PROCESAMIENTO DE COMANDO: comando_validar_propiedad ***********")
    data=mensaje.value().data 
    print(f'AUDITORIA - Comando recibido: {data}')
    id_propiedad = data.id_propiedad
    servicio_propiedades = ServicioExternoPropiedades()
    auditoria_propiedad_dict=servicio_propiedades.obtener_datos(id_propiedad=id_propiedad)
    map_auditoria = MapeadorAuditoriaDTOJson()
    auditoria_propiedad_dto = map_auditoria.externo_a_dto(auditoria_propiedad_dict)
    fabrica_auditoria = FabricaAuditoria()
    auditoria: Auditoria = fabrica_auditoria.crear_objeto(auditoria_propiedad_dto, MapeadorAuditoria())
    propiedad_validada=auditoria.validar_propiedad(auditoria)
    evento_propiedad_validada= EventoPropiedadValidada(id_propiedad=id_propiedad, estado=propiedad_validada.estado, campos_faltantes=propiedad_validada.campos_faltantes) 
    dispatcher.send(signal=f'{type(evento_propiedad_validada).__name__}Dominio', evento=evento_propiedad_validada)
    print(f'AUDITORIA - Evento enviado: {evento_propiedad_validada}')
    print("*********** AUDITORIA - FIN PROCESAMIENTO DE COMANDO: comando_validar_propiedad ***********")    

def comando_revertir_validacion(mensaje):
    ...