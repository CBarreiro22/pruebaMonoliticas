import uuid
from dataclasses import dataclass
from typing import List

from propiedadDeLosAlpes.seedwork.dominio.eventos import EventoDominio


@dataclass
class EventoPropiedadValidada(EventoDominio):
    id_propiedad: uuid.UUID = None
    estado: str = None
    campos_faltantes: List[str] = None

@dataclass
class ResultadosValidacionAgente(EventoDominio):
    id_propiedad: uuid.UUID = None
    campos_faltantes: List[str] = None

@dataclass
class ValidacionPropiedadFallida(EventoDominio):
    id_propiedad: uuid.UUID = None
    mensaje: str = None