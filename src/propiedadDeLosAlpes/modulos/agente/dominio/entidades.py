from __future__ import annotations
import uuid
from dataclasses import dataclass, field
import propiedadDeLosAlpes.modulos.agente.dominio.objetos_valor as ov
from propiedadDeLosAlpes.modulos.agente.dominio.eventos import PropiedadCompletada
from propiedadDeLosAlpes.seedwork.dominio.entidades import AgregacionRaiz
from typing import Dict


@dataclass
class PropiedadCompletada(AgregacionRaiz):
    id_propiedad: int = field(default=0)
    campos_faltantes: str = field(default_factory=str)
 


    def crear_propiedad_completada(self, completar_propiedad: PropiedadCompletada):
        self.agregar_evento(
            PropiedadCompletada(id_propiedad=self.id))