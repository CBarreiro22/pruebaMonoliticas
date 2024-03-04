
from .mensajes import Mensaje
from pulsar.schema import *
from propiedadDeLosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
import uuid
class EventoPropiedad(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoPropiedadRegistrada")
    datacontenttype = String()
    service_name = String(default="propiedad.propiedadDeLosAlpes")
    id_propiedad = id_propiedad
    campos_faltantes = campos_faltantes


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)