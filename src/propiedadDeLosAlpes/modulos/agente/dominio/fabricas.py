from .entidades import PropiedadCompletada
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadExcepcion
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from propiedadDeLosAlpes.seedwork.dominio.fabricas import Fabrica
from propiedadDeLosAlpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaPropiedad(Fabrica):

    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: PropiedadCompletada = mapeador.dto_a_entidad(obj)

            return propiedad


@dataclass
class FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == PropiedadCompletada.__class__:
            fabrica_propiedad = _FabricaPropiedad()
            return fabrica_propiedad.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadExcepcion()
