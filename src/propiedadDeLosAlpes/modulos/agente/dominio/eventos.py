import uuid
from dataclasses import dataclass
from datetime import datetime

from propiedadDeLosAlpes.seedwork.dominio.eventos import EventoDominio


@dataclass
class PropiedadEnriquecida(EventoDominio):
    id_propiedad: uuid.UUID = None
    propiedades_completadas : str=None

@dataclass
class PropiedadNoCreada(EventoDominio):
    id_propiedad: uuid.UUID = None
