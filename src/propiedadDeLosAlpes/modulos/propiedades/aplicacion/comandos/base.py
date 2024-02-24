from src.propiedadDeLosAlpes.modulos.propiedades.dominio.fabricas import FabricaPropiedad
from src.propiedadDeLosAlpes.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from src.propiedadDeLosAlpes.seedwork.aplicacion.comandos import ComandoHandler


class CrearPropiedadBaseHandler (ComandoHandler):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vpropiedades: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades