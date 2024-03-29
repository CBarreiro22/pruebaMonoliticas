from pulsar.schema import *
from propiedadDeLosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class EventoPropiedadCreadaPayload(Record):
    id_propiedad = String()
    
class EventoPropiedadCreada(EventoIntegracion):
    data = EventoPropiedadCreadaPayload()

class EventoPropiedadRegistradaAgentePayload(Record):
    id_propiedad = String()
    campos_faltantes= Array(String())

class EventoPropiedadRegistradaAgente(EventoIntegracion):
    data = EventoPropiedadRegistradaAgentePayload()

class EventoPropiedadHabilitadaPayload(Record):
    id_propiedad = String()

class EventoPropiedadHabilitada(EventoIntegracion):
    data = EventoPropiedadHabilitadaPayload()

class EventoPropiedadNoCreadaPayload(Record):
    id_propiedad = String()

class EventoPropiedadNoCreada(EventoIntegracion):
    data = EventoPropiedadNoCreadaPayload()

class EventoValidacionPropiedadFallidaPayload(Record):
    id_propiedad = String()
    mensaje = String()

class EventoValidacionPropiedadFallida(EventoIntegracion):
    data = EventoValidacionPropiedadFallidaPayload()


