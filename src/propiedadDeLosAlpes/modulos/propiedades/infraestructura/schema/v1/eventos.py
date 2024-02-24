


class ReservaCreadaPayload(Record):
    id_propiedad = String()
    id_propietario = String()
    estado = String()
    fecha_creacion = Long()
    tipo_propiedad = String()

class EventoReservaCreada(EventoIntegracion):
    data = ReservaCreadaPayload()