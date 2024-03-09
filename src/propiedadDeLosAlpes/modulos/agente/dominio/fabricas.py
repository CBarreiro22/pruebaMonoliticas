from .entidades import Agente
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadExcepcion
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador
from propiedadDeLosAlpes.seedwork.dominio.fabricas import Fabrica
from propiedadDeLosAlpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaAgente(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            agente: Agente = mapeador.dto_a_entidad(obj)
            return agente

@dataclass
class FabricaAgente(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Agente.__class__:
            fabrica_agente = _FabricaAgente()
            return fabrica_agente.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadExcepcion()
