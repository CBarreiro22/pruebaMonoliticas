from propiedadDeLosAlpes.seedwork.aplicacion.handlers import Handler
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.despachadores import Despachador

class HandlerAuditoriaDominio(Handler):

    @staticmethod
    def handle_propiedad_modificada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad-validada')
    
    @staticmethod
    def handle_evento_propiedad_validada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'evento_propiedad_validada')

    @staticmethod
    def handle_comando_cancelar_creacion_propiedad(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'comando_cancelar_creacion_propiedad')
        

    