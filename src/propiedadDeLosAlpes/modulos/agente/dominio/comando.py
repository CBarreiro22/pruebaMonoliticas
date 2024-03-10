import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List
from propiedadDeLosAlpes.seedwork.dominio.eventos import EventoDominio

@dataclass
class RevertirValidacionPropiedad(EventoDominio):
    id_propiedad: uuid.UUID = None