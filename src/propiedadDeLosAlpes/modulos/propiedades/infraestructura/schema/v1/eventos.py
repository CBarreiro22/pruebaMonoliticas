from pulsar.schema import *
from propiedadDeLosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class PropiedadCreadaPayload(Record):
    id_propiedad = String()
class EventoPropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()
class EventoPropiedadRegistradaAgentePayload(Record):
    id_propiedad = String()
    campos_faltantes= Array(String)
class EventoPropiedadRegistradaAgente(EventoIntegracion):
    data = PropiedadCreadaPayload()
    