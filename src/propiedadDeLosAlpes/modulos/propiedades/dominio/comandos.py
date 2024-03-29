import uuid
from dataclasses import dataclass
from datetime import datetime

from propiedadDeLosAlpes.seedwork.dominio.eventos import EventoDominio


@dataclass
class ComandoValidarPropiedad(EventoDominio):
    id_propiedad: uuid.UUID = None

@dataclass
class RevertirEnriquecimientoPropiedad(EventoDominio):
    id_propiedad: uuid.UUID = None
