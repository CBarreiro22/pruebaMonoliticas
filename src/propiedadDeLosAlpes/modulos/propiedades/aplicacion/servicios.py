from propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.fabricas import FabricaPropiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from propiedadDeLosAlpes.seedwork.aplicacion.servicios import Servicio

class ServicioPropiedades(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades  
    
    def obtener_propiedad_por_id(self, id) -> PropiedadDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        return self.fabrica_propiedades.crear_objeto(repositorio.obtener_por_id(id), MapeadorPropiedad())

