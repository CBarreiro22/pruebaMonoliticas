from src.propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from src.propiedadDeLosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap


class   MapeadorPropiedadDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        pass