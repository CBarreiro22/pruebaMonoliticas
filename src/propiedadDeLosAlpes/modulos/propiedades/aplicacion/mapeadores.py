from src.propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from src.propiedadDeLosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from src.propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap


class   MapeadorPropiedadDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()

        return propiedad_dto


class MapeadorPropiedad(RepMap):
    pass