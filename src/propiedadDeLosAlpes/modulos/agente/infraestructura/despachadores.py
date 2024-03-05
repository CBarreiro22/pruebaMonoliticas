import pulsar
from pulsar.schema import *
from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import EventoPropiedadCompletada,PropiedadCompletadaPayload
from propiedadDeLosAlpes.seedwork.infraestructura import utils
import datetime

from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import PropiedadRegistradaPayload

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadCompletada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = PropiedadCompletadaPayload(
            id_propiedad=str(evento.id_propiedad),
            propiedades_completadas=evento.propiedades_completadas
        )
        evento_dominio = EventoPropiedadCompletada(data=payload)
        self._publicar_mensaje(evento_dominio, topico, AvroSchema(EventoPropiedadCompletada))

    def publicar_evento_propiedad_registrada(self, evento, topico):
        
        payload = PropiedadRegistradaPayload(
            id_propiedad=str(evento.id_propiedad),
            propiedades_completadas=evento.campos_faltantes
        )
        evento_dominio = EventoPropiedadRegistrada(data=payload)
        self._publicar_mensaje(evento_dominio, topico, AvroSchema(EventoPropiedadRegistrada))
