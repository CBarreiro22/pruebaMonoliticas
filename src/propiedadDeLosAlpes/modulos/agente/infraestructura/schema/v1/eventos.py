from pulsar.schema import *
from propiedadDeLosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadRegistradaPayload(Record):
    id_propiedad = String()
    campos_faltantes = Array(String())
    

class EventoPropiedadRegistrada(EventoIntegracion):
    data = PropiedadRegistradaPayload()


class PropiedadCompletadaPayload(Record):
    id_propiedad = String()
    propiedades_completadas = String()


class EventoPropiedadCompletada(EventoIntegracion):
    data = PropiedadCompletadaPayload()