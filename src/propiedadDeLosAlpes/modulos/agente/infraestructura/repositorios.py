
""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de propiedad

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de propiedad

"""

from propiedadDeLosAlpes.config.db import db
from propiedadDeLosAlpes.modulos.agente.dominio.repositorios import RepositorioAgente
from propiedadDeLosAlpes.modulos.agente.dominio.entidades import Agente
from propiedadDeLosAlpes.modulos.agente.dominio.fabricas import FabricaAgente
from .dto import Agente as AgenteDTO
from .mapeadores import MapeadorAgente
from uuid import UUID

class RepositorioAgentePostgreSQL(RepositorioAgente):

    def __init__(self):
        self._fabrica_agente: FabricaAgente = FabricaAgente()

    @property
    def fabrica_agente(self):
        return self._fabrica_agente

    def obtener_por_id(self, id: UUID) -> Agente:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Agente]:
        # TODO
        raise NotImplementedError

    def agregar(self, agente: Agente):
        agente_dto = self.fabrica_agente.crear_objeto(agente, MapeadorAgente())
        db.session.add(agente_dto)
        db.session.commit()
    
    def actualizar(self, agente: Agente):
        # TODO
        raise NotImplementedError

    def eliminar(self, agente_id: UUID):
        # TODO
        raise NotImplementedError