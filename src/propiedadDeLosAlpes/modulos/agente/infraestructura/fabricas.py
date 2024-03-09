from dataclasses import dataclass

from propiedadDeLosAlpes.modulos.agente.dominio.repositorios import RepositorioAgente
from propiedadDeLosAlpes.modulos.agente.infraestructura.repositorios import RepositorioAgentePostgreSQL
from propiedadDeLosAlpes.seedwork.dominio.excepciones import ExcepcionFabrica
from propiedadDeLosAlpes.seedwork.dominio.fabricas import Fabrica
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAgente.__class__:
            return RepositorioAgentePostgreSQL()
        else:
            raise ExcepcionFabrica()