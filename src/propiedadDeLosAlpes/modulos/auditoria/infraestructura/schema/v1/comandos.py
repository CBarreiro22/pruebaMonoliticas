from pulsar.schema import *
from propiedadDeLosAlpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
import uuid
from propiedadDeLosAlpes.seedwork.infraestructura.utils import time_millis
    
class ComandoCancelarCreacionPropiedadPayload(Record):
    id_propiedad = String()

class ComandoCancelarCreacionPropiedad(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="CancelarCreacionPropiedad")
    datacontenttype = String()
    service_name = String(default="propiedadDeLosAlpes")
    data = ComandoCancelarCreacionPropiedadPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)