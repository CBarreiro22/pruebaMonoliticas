import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class PropiedadCreada(EventoDominio):
    id_propiedad: uuid.UUID = None
    id_propietario: uuid.UUID = None
    tipo_propiedad: str = None
    estado: str = None
    fecha_creacion: datetime = None