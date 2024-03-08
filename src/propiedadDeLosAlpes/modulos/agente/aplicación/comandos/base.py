from propiedadDeLosAlpes.modulos.agente.dominio.fabricas import FabricaPropiedad
from propiedadDeLosAlpes.modulos.agente.infraestructura.fabricas import FabricaRepositorio
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ComandoHandler


class  CompletarPropiedadBaseHandler (ComandoHandler):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades