import uuid
from dataclasses import dataclass
from datetime import datetime

from propiedadDeLosAlpes.seedwork.dominio.eventos import EventoDominio


@dataclass
class PropiedadCompletada(EventoDominio):
    id_propiedad: uuid.UUID = None