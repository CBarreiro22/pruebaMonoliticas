from pulsar.schema import *
from propiedadDeLosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadModificadaPayload(Record):
    id_propiedad = String()
    estado = String()
    campos_faltantes = Array(String)
    

class EventoPropiedadModificada(EventoIntegracion):
    data = PropiedadModificadaPayload()