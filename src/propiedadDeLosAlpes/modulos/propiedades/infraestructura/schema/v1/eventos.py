from pulsar.schema import *
from propiedadDeLosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from propiedadDeLosAlpes.seedwork.dominio.eventos import EventoDominio


class PropiedadCreadaPayload(Record):
    id_propiedad = String()

class EventoPropiedadCreada(EventoDominio):
    data = PropiedadCreadaPayload()