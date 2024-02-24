

""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from propiedadDeLosAlpes.config.db import db
from propiedadDeLosAlpes.modulos.vuelos.dominio.repositorios import RepositorioPropiedads, RepositorioProveedores
from propiedadDeLosAlpes.modulos.vuelos.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from propiedadDeLosAlpes.modulos.vuelos.dominio.entidades import Proveedor, Aeropuerto, Propiedad
from propiedadDeLosAlpes.modulos.vuelos.dominio.fabricas import FabricaVuelos
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedad
from uuid import UUID

from propiedadDeLosAlpes.modulos.propiedades.dominio.fabricas import FabricaPropiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades

from ..aplicacion.dto import PropiedadDTO
from ..aplicacion.mapeadores import MapeadorPropiedad
from ..dominio.entidades import Propiedad


class RepositorioPropiedadesSQLite(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_propiedad: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_vuelos.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_vuelos.crear_objeto(propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)

    def actualizar(self, propiedad: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        # TODO
        raise NotImplementedError