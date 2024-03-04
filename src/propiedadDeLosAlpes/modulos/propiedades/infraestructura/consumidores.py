from propiedadDeLosAlpes.modulos.auditoria.dominio.eventos import ResultadosValidacionAgente
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from propiedadDeLosAlpes.seedwork.infraestructura import utils

from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.schema.v1.eventos import EventoPropiedadModificada
from pydispatch import dispatcher

def suscribirse_a_eventos():
    suscribirse_a_eventos_auditoria()
    suscribirse_a_eventos_agente()
        
def suscribirse_a_eventos_agente():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad-complementada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadModificada))
        while True:
            mensaje = consumidor.receive()
            data=mensaje.value().data
            print(f'Evento recibido: {data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventos_auditoria():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad-validada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadModificada))
        #eventos-propiedad-validada
        #eventos-propiedad-complementada
        while True:
            mensaje = consumidor.receive()
            data=mensaje.value().data
            print("*********** Benito **********")
            print(f'Evento recibido propiedad validada: {data}')
            print(data.id_propiedad)
            print(data.estado)
            print(data.campos_faltantes)
            
            #Insertar en la base de datos pa actualizar el estado de la propiedad
            #fabrica_propiedades = FabricaPropiedades()
            #propiedades: Propiedades = fabrica_propiedades.crear_objeto(auditoria_propiedad_dto, MapeadorPropiedades())
            
            #propiedad_actualizada=propiedades.actualizar_propiedad(propiedades)
            #Generar evento para el modulo Agente ... aunque no debería estar aqui
            #Si el estado es faltan datos, deberia lanzarse el avento para que agente lo procese ... y como un todo (UoW)
            if data.estado == "faltan_datos":
                evento_resultado_validacion_agente= ResultadosValidacionAgente(id_propiedad=data.id_propiedad,  campos_faltantes=data.campos_faltantes)
                dispatcher.send(signal=f'{type(evento_resultado_validacion_agente).__name__}Dominio', evento=evento_resultado_validacion_agente)
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
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