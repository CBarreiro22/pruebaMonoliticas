from __future__ import annotations
from dataclasses import dataclass, field
from propiedadDeLosAlpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class CreacionPropiedadFallida(EventoDominio):
    id_propiedad: uuid.UUID = None

@dataclass
class ValidacionPropiedadFallida(EventoDominio):
    id_propiedad: uuid.UUID = None

@dataclass
class EnriquecimientoPropiedadFallida(EventoDominio):
    id_propiedad: uuid.UUID = None

@dataclass
class HabilitacionPropiedadFallida(EventoDominio):
    id_propiedad: uuid.UUID = None

