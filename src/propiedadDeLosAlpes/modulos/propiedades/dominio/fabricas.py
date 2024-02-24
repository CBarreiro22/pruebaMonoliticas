from dataclasses import dataclass

from propiedadDeLosAlpes.seedwork.dominio.entidades import Entidad
from propiedadDeLosAlpes.seedwork.dominio.fabricas import Fabrica
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador
from .entidades import Propiedad
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadExcepcion


@dataclass
class _FabricaPropiedad(Fabrica):

    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)

            return propiedad


@dataclass
class FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_propiedad = _FabricaPropiedad()
            return fabrica_propiedad.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadExcepcion()
