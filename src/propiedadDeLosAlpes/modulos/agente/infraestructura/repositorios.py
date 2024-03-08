
""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de propiedad

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de propiedad

"""

from propiedadDeLosAlpes.config.db import db
from propiedadDeLosAlpes.modulos.agente.dominio.repositorios import RepositorioPropiedadesCompletadas
from propiedadDeLosAlpes.modulos.agente.dominio.entidades import PropiedadCompletada
from propiedadDeLosAlpes.modulos.agente.dominio.fabricas import FabricaPropiedad
from .dto import PropiedadCompletada as PropiedadDTO
from .mapeadores import MapeadorPropiedadCompletada
from uuid import UUID


class RepositorioPropiedadesSQLite(RepositorioPropiedadesCompletadas):

    def __init__(self):
        self._fabrica_propiedad: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad

    def obtener_por_id(self, id: UUID) -> PropiedadCompletada:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedad.crear_objeto(propiedad_dto, MapeadorPropiedadCompletada())

    def obtener_todos(self) -> list[PropiedadCompletada]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: PropiedadCompletada):
        propiedad_dto = self.fabrica_propiedad.crear_objeto(propiedad, MapeadorPropiedadCompletada())
        db.session.add(propiedad_dto)

    def actualizar(self, propiedad: PropiedadCompletada):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        # TODO
        raise NotImplementedError

class RepositorioPropiedadesPostgreSQL(RepositorioPropiedadesCompletadas):

    def __init__(self):
        self._fabrica_propiedad: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad

    def obtener_por_id(self, id: UUID) -> PropiedadCompletada:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedad.crear_objeto(propiedad_dto, MapeadorPropiedadCompletada())

    def obtener_todos(self) -> list[PropiedadCompletada]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: PropiedadCompletada):
        propiedad_dto = self.fabrica_propiedad.crear_objeto(propiedad, MapeadorPropiedadCompletada())
        db.session.add(propiedad_dto)
        db.session.commit()
    
    def actualizar(self, propiedad: PropiedadCompletada):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        # TODO
        raise NotImplementedError