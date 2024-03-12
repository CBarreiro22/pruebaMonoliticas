from propiedadDeLosAlpes.seedwork.aplicacion.handlers import Handler
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.despachadores import Despachador

class HandlerAuditoriaDominio(Handler):

    # @staticmethod
    # def handle_propiedad_modificada(evento):
    #     despachador = Despachador()
    #     despachador.publicar_evento(evento, 'eventos-propiedad-validada')
    
    @staticmethod
    def handle_evento_propiedad_validada(evento):
        despachador = Despachador()
        despachador.publicar_evento_propiedad_validada(evento, 'evento-propiedad-validada')

    @staticmethod
    def handle_comando_cancelar_creacion_propiedad(evento):
        despachador = Despachador()
        despachador.publicar_comando_cancelar_creacion_propiedad(evento, 'comando-cancelar-creacion-propiedad')
        

    