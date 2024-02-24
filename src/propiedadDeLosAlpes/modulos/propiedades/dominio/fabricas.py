from dataclasses import dataclass

from src.propiedadDeLosAlpes.seedwork.dominio.fabricas import Fabrica
from src.propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador
from .entidades import Propiedad
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadExcepcion


@dataclass
class _FabricaPropiedad(Fabrica):
    pass

@dataclass
class FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_propiedad = _FabricaPropiedad()
            return fabrica_propiedad.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadExcepcion()
