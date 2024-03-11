from propiedadDeLosAlpes.modulos.auditoria.dominio.fabricas import FabricaAuditoria
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.fabricas import FabricaRepositorio
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ComandoHandler


class AuditoriaBaseHandler (ComandoHandler):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditoria: FabricaAuditoria = FabricaAuditoria()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_auditoria(self):
        return self._fabrica_auditoria