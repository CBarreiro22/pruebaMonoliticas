import pulsar
from pulsar.schema import *
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada,PropiedadCreadaPayload, EventoPropiedadRegistradaAgente, EventoPropiedadRegistradaAgentePayload
from propiedadDeLosAlpes.seedwork.infraestructura import utils
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = PropiedadCreadaPayload(
            id_propiedad=str(evento.id_propiedad),
        )
        evento_dominio = EventoPropiedadCreada(data=payload)
        self._publicar_mensaje(evento_dominio, topico, AvroSchema(EventoPropiedadCreada))
    
    def _publicar_mensaje_agente(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadRegistradaAgente))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento_agente(self, evento, topico):
        payload = EventoPropiedadRegistradaAgentePayload(
            id_propiedad=str(evento.id_propiedad),
            campos_faltantes=evento.campos_faltantes
        )
        evento_dominio = EventoPropiedadRegistradaAgente(data=payload)
        self._publicar_mensaje_agente(evento_dominio, topico, AvroSchema(EventoPropiedadRegistradaAgente))
