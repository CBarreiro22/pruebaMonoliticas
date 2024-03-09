from __future__ import annotations
import uuid
from dataclasses import dataclass, field
import propiedadDeLosAlpes.modulos.agente.dominio.objetos_valor as ov
from propiedadDeLosAlpes.modulos.agente.dominio.eventos import EventoPropiedadEnriquecida
from propiedadDeLosAlpes.seedwork.dominio.entidades import AgregacionRaiz
from typing import Dict


@dataclass
class PropiedadEnriquecida(AgregacionRaiz):
    id_propiedad: int = field(default=0)
    campos_enriquecidos: str = field(default_factory=str)
 


    def crear_propiedad_completada(self, propiedad_enriquezida: PropiedadEnriquecida):
        self.agregar_evento(
            EventoPropiedadEnriquecida(id_propiedad=self.id_propiedad, campos_enriquecidos=self.campos_enriquecidos))