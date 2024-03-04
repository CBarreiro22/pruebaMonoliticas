from dataclasses import dataclass

from propiedadDeLosAlpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedadesPostgreSQL
from propiedadDeLosAlpes.seedwork.dominio.excepciones import ExcepcionFabrica
from propiedadDeLosAlpes.seedwork.dominio.fabricas import Fabrica
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadesPostgreSQL()
        else:
            raise ExcepcionFabrica()