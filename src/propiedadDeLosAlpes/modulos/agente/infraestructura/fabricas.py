from dataclasses import dataclass

from propiedadDeLosAlpes.modulos.agente.dominio.repositorios import RepositorioPropiedadesCompletadas
from propiedadDeLosAlpes.modulos.agente.infraestructura.repositorios import RepositorioPropiedadesPostgreSQL
from propiedadDeLosAlpes.seedwork.dominio.excepciones import ExcepcionFabrica
from propiedadDeLosAlpes.seedwork.dominio.fabricas import Fabrica
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedadesCompletadas.__class__:
            return RepositorioPropiedadesPostgreSQL()
        else:
            raise ExcepcionFabrica()