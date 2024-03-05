from propiedadDeLosAlpes.seedwork.aplicacion.handlers import Handler
from propiedadDeLosAlpes.modulos.agente.infraestructura.despachadores import Despachador

class HandlerPropiedadCompletadaDominio(Handler):

    @staticmethod
    def handle_evento_propiedad_completada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad-complementada')
        

    