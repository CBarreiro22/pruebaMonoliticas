from pulsar.schema import *
from propiedadDeLosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadValidadaPayload(Record):
    id_propiedad = String()
    estado = String()
    campos_faltantes = Array(String())
    

class EventoPropiedadValidada(EventoIntegracion):
    data = PropiedadValidadaPayload()