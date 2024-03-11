import pulsar
from pulsar.schema import *
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada, EventoPropiedadCreadaPayload, EventoPropiedadRegistradaAgente, EventoPropiedadRegistradaAgentePayload, EventoPropiedadHabilitada, EventoPropiedadHabilitadaPayload
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoValidarPropiedad, ComandoValidarPropiedadPayload, ComandoEnriquecerPropiedad, ComandoEnriquecerPropiedadPayload, ComandoRevertirEnriquecimientoPropiedad, ComandoRevertirEnriquecimientoPropiedadPayload
from propiedadDeLosAlpes.seedwork.infraestructura import utils
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    # def _publicar_mensaje(self, mensaje, topico, schema):
    #     cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
    #     publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadCreada))
    #     publicador.send(mensaje)
    #     cliente.close()

    # def publicar_evento(self, evento, topico):
    #     payload = PropiedadCreadaPayload(
    #         id_propiedad=str(evento.id_propiedad),
    #     )
    #     evento_dominio = EventoPropiedadCreada(data=payload)
    #     self._publicar_mensaje(evento_dominio, topico, AvroSchema(EventoPropiedadCreada))
    
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

    #comando_validar_propiedad
    def _publicar_comando_validar_propiedad(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoValidarPropiedad))
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando_validar_propiedad(self, evento, topico):
        payload = ComandoValidarPropiedadPayload(
            id_propiedad=str(evento.id_propiedad)
        )
        comando = ComandoValidarPropiedad(
            time=utils.time_millis(),
            ingestion=utils.time_millis(),
            datacontenttype=ComandoValidarPropiedadPayload.__name__,
            data=payload
        )
        self._publicar_comando_validar_propiedad(comando, topico, AvroSchema(ComandoValidarPropiedad))
    
    #comando_enriquecer_propiedad
    def _publicar_comando_enriquecer_propiedad(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoEnriquecerPropiedad))
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando_enriquecer_propiedad(self, evento, topico):
        payload = ComandoEnriquecerPropiedadPayload(
            id_propiedad=str(evento.id_propiedad),
            campos_faltantes=evento.campos_faltantes
        )
        comando = ComandoEnriquecerPropiedad(data=payload)
        self._publicar_comando_enriquecer_propiedad(comando, topico, AvroSchema(ComandoEnriquecerPropiedad))
    
    #comando_revertir_enriquecimiento
    def _publicar_comando_revertir_enriquecimiento(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoRevertirEnriquecimientoPropiedad))
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando_revertir_enriquecimiento(self, evento, topico):
        payload = ComandoRevertirEnriquecimientoPropiedadPayload(
            id_propiedad=str(evento.id_propiedad)
        )
        comando = ComandoRevertirEnriquecimientoPropiedad(data=payload)
        self._publicar_comando_revertir_enriquecimiento(comando, topico, AvroSchema(ComandoRevertirEnriquecimientoPropiedad))
    
    #evento_propiedad_creada
    def _publicar_evento_propiedad_creada(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento_propiedad_creada(self, evento, topico):
        payload = EventoPropiedadCreadaPayload(
            id_propiedad=str(evento.id_propiedad)
        )
        evento = EventoPropiedadCreada(data=payload)
        self._publicar_evento_propiedad_creada(evento, topico, AvroSchema(EventoPropiedadCreada))

    #evento_propiedad_habilitada
    def _publicar_evento_propiedad_habilitada(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadHabilitada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento_propiedad_habilitada(self, evento, topico):
        payload = EventoPropiedadHabilitadaPayload(
            id_propiedad=str(evento.id_propiedad)
        )
        evento = EventoPropiedadHabilitada(data=payload)
        self._publicar_evento_propiedad_habilitada(evento, topico, AvroSchema(EventoPropiedadHabilitada))