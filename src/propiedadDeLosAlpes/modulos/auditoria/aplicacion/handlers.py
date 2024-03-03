from propiedadDeLosAlpes.seedwork.aplicacion.handlers import Handler
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.despachadores import Despachador

class HandlerPropiedadModificadaDominio(Handler):

    @staticmethod
    def handle_propiedad_modificada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad-validada')

        

    