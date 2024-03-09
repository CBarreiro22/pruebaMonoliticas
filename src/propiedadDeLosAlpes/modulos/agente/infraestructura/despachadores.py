import pulsar
from pulsar.schema import *
from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import EventoPropiedadEnriquecida, EventoPropiedadEnriquecidaPayload
from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.comandos import ComandoRevertirValidacionPropiedad, ComandoRevertirValidacionPropiedadPayload

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

    #evento_propiedad_enriquecida
    def _publicar_evento_propiedad_enriquecida(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadEnriquecida))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento_propiedad_enriquecida(self, evento, topico):
        payload = EventoPropiedadEnriquecidaPayload(
            id_propiedad=str(evento.id_propiedad),
            propiedades_completadas=evento.propiedades_completadas
        )
        evento_dominio = EventoPropiedadEnriquecida(data=payload)
        self._publicar_evento_propiedad_enriquecida(evento_dominio, topico, AvroSchema(EventoPropiedadEnriquecida))
    
    #comando_revertir_validacion
    def _publicar_comando_revertir_validacion(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoRevertirValidacionPropiedad))
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando_revertir_validacion(self, evento, topico):
        payload = ComandoRevertirValidacionPropiedadPayload(
            id_propiedad=str(evento.id_propiedad)
        )
        comando = ComandoRevertirValidacionPropiedad(data=payload)
        self._publicar_comando_revertir_validacion(comando, topico, AvroSchema(ComandoRevertirValidacionPropiedad))
