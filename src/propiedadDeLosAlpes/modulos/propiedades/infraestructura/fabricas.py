from dataclasses import dataclass

from src.propiedadDeLosAlpes.seedwork.dominio.fabricas import Fabrica
from src.propiedadDeLosAlpes.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioReservas.__class__:
            return RepositorioReservasSQLite()
        elif obj == RepositorioProveedores.__class__:
            return RepositorioProveedoresSQLite()
        else:
            raise ExcepcionFabrica()