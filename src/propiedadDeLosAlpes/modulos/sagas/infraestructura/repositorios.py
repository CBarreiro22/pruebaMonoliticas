
""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de propiedad

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de propiedad

"""

from propiedadDeLosAlpes.config.db import db
from propiedadDeLosAlpes.modulos.sagas.dominio.repositorios import RepositorioSaga
from propiedadDeLosAlpes.modulos.sagas.dominio.entidades import Saga
from propiedadDeLosAlpes.modulos.sagas.dominio.fabricas import FabricaSaga
from .dto import Saga as SagaDTO
from .mapeadores import MapeadorSaga
from uuid import UUID


class RepositorioSagaPostgreSQL(RepositorioSaga):

    def __init__(self):
        self._fabrica_saga: FabricaSaga = FabricaSaga()

    @property
    def fabrica_propiedad(self):
        return self._fabrica_saga

    def obtener_por_id(self, id: UUID) -> Saga:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Saga]:
        # TODO
        raise NotImplementedError

    def agregar(self, saga: Saga):
        saga_dto = self.fabrica_propiedad.crear_objeto(saga, MapeadorSaga())
        db.session.add(saga_dto)
        db.session.commit()
    
    def actualizar(self, saga: Saga):
        # TODO
        raise NotImplementedError

    def eliminar(self, saga_id: UUID):
        # TODO
        raise NotImplementedError