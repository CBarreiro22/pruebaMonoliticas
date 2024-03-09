from pulsar.schema import *
from propiedadDeLosAlpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
import uuid
from propiedadDeLosAlpes.seedwork.infraestructura.utils import time_millis

class ComandoCrearPropiedadPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()

class ComandoValidarPropiedadPayload(Record):
    id_propiedad = String()

class ComandoValidarPropiedad(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ValidarPropiedad")
    datacontenttype = String()
    service_name = String(default="propiedadDeLosAlpes")
    data = ComandoValidarPropiedadPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoEnriquecerPropiedadPayload(Record):
    id_propiedad = String()
    campos_faltantes = Array(String())

class ComandoEnriquecerPropiedad(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EnriquecerPropiedad")
    datacontenttype = String()
    service_name = String(default="propiedadDeLosAlpes")
    data = ComandoEnriquecerPropiedadPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
class ComandoRevertirEnriquecimientoPropiedadPayload(Record):
    id_propiedad = String()

class ComandoRevertirEnriquecimientoPropiedad(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="RevertirEnriquecimientoPropiedad")
    datacontenttype = String()
    service_name = String(default="propiedadDeLosAlpes")
    data = ComandoRevertirEnriquecimientoPropiedadPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)