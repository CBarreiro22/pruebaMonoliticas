from __future__ import annotations
import uuid
from dataclasses import dataclass, field
import propiedadDeLosAlpes.modulos.agente.dominio.objetos_valor as ov
from propiedadDeLosAlpes.seedwork.dominio.entidades import AgregacionRaiz
from propiedadDeLosAlpes.modulos.agente.dominio.eventos import PropiedadEnriquecida

@dataclass
class Agente(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=None)
    propiedades_completadas: str = field(default=None)
    
    def crear_agente_propiedad(self, agente: Agente):
        self.agregar_evento(
            PropiedadEnriquecida(id_propiedad=agente.id_propietario, propiedades_completadas=agente.propiedades_completadas))