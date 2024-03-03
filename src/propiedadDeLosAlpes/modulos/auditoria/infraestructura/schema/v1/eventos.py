from pulsar.schema import *
from propiedadDeLosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadModificadaPayload(Record):
    id_propiedad = String()
    id_xxx = String()
    estado = String()
    fecha_creacion = Long()

class EventoPropiedadModificada(EventoIntegracion):
    data = PropiedadModificadaPayload()