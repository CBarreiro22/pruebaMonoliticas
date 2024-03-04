from dataclasses import dataclass
from typing import List

from propiedadDeLosAlpes.seedwork.dominio.eventos import EventoDominio


@dataclass
class ResultadosValidacion(EventoDominio):
    id_propiedad: uuid.UUID = None
    estado: str = None
    campos_faltantes: List[str] = None