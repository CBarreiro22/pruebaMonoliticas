from dataclasses import dataclass, field
from typing import Dict
from propiedadDeLosAlpes.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class PropiedadCompletadaDTO(DTO):
    id: str = field(default_factory=str)
    campos_faltantes: str = field(default_factory=str)
