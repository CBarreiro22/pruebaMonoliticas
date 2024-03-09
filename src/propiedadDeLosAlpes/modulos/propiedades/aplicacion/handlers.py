from propiedadDeLosAlpes.seedwork.aplicacion.handlers import Handler
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerPropiedadDominio(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad-modificada')
    
    @staticmethod
    def handle_propiedad_validacion_agente(evento):
        despachador = Despachador()
        despachador.publicar_evento_agente(evento, 'eventos-propiedad-registrada')

    @staticmethod
    def handle_comando_validar_propiedad(evento):
        despachador = Despachador()
        despachador.publicar_evento_agente(evento, 'comando_validar_propiedad')
    
    @staticmethod
    def handle_comando_enriquecer_propiedad(evento):
        despachador = Despachador()
        despachador.publicar_evento_agente(evento, 'comando_enriquecer_propiedad')
    
    @staticmethod
    def handle_evento_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento_agente(evento, 'evento_propiedad_creada')