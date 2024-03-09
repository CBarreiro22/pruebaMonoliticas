import pulsar
from pulsar.schema import *
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.schema.v1.eventos import EventoPropiedadValidada,PropiedadValidadaPayload
from propiedadDeLosAlpes.seedwork.infraestructura import utils
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadValidada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = PropiedadValidadaPayload(
            id_propiedad=str(evento.id_propiedad), 
            estado=str(evento.estado),
            campos_faltantes=[str(campo) for campo in evento.campos_faltantes]
        )
        evento_dominio = EventoPropiedadValidada(data=payload)
        self._publicar_mensaje(evento_dominio, topico, AvroSchema(EventoPropiedadValidada))
    
    #evento_propiedad_validada
    def _publicar_evento_propiedad_validada(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadValidada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento_propiedad_validada(self, evento, topico):
        payload = PropiedadValidadaPayload(
            id_propiedad=str(evento.id_propiedad), 
            estado=str(evento.estado),
            campos_faltantes=[str(campo) for campo in evento.campos_faltantes]
        )
        evento_dominio = EventoPropiedadValidada(data=payload)
        self._publicar_evento_propiedad_validada(evento_dominio, topico, AvroSchema(EventoPropiedadValidada))
    
    #comando_cancelar_creacion_propiedad
    def _publicar_comando_cancelar_creacion_propiedad(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadValidada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando_cancelar_creacion_propiedad(self, evento, topico):
        payload = PropiedadValidadaPayload(
            id_propiedad=str(evento.id_propiedad), 
            estado=str(evento.estado),
            campos_faltantes=[str(campo) for campo in evento.campos_faltantes]
        )
        evento_dominio = EventoPropiedadValidada(data=payload)
        self._publicar_comando_cancelar_creacion_propiedad(evento_dominio, topico, AvroSchema(EventoPropiedadValidada))
