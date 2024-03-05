from propiedadDeLosAlpes.seedwork.aplicacion.handlers import Handler
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerPropiedadCreadaDominio(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad-modificada')
    
    @staticmethod
    def handle_propiedad_validacion_agente(evento):
        despachador = Despachador()
        despachador.publicar_evento_agente(evento, 'eventos-propiedad-registrada')


