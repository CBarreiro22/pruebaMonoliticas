
""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de propiedad

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de propiedad

"""

from propiedadDeLosAlpes.config.db import db
from propiedadDeLosAlpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from propiedadDeLosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.fabricas import FabricaPropiedad
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedad
from uuid import UUID


class RepositorioPropiedadesSQLite(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_propiedad: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedad.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_propiedad.crear_objeto(propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)

    def actualizar(self, propiedad: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        # TODO
        raise NotImplementedError

class RepositorioPropiedadesPostgreSQL(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_propiedad: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedad.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_propiedad.crear_objeto(propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)
    
    def actualizar(self, propiedad: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        # TODO
        raise NotImplementedError