from dataclasses import dataclass

from src.propiedadDeLosAlpes.seedwork.dominio.fabricas import Fabrica
from src.propiedadDeLosAlpes.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadesSQLite()
        else:
            raise ExcepcionFabrica()