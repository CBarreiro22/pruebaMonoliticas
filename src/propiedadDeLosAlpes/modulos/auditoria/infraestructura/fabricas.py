from dataclasses import dataclass

from propiedadDeLosAlpes.modulos.auditoria.dominio.repositorios import RepositorioAuditoria
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.repositorios import RepositorioAuditoriaPostgreSQL
from propiedadDeLosAlpes.seedwork.dominio.excepciones import ExcepcionFabrica
from propiedadDeLosAlpes.seedwork.dominio.fabricas import Fabrica
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAuditoria.__class__:
            return RepositorioAuditoriaPostgreSQL()
        else:
            raise ExcepcionFabrica()