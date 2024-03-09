from propiedadDeLosAlpes.seedwork.aplicacion.handlers import Handler
from propiedadDeLosAlpes.modulos.agente.infraestructura.despachadores import Despachador

class HandlerAgenteDominio(Handler):

    @staticmethod
    def handle_evento_propiedad_completada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad-complementada')
    
    @staticmethod
    def handle_evento_propiedad_enriquecida(evento):
        print("Benito handler")
        despachador = Despachador()
        despachador.publicar_evento_propiedad_enriquecida(evento, 'evento-propiedad-enriquecida')
    
    @staticmethod
    def handle_comando_revertir_validacion(evento):
        despachador = Despachador()
        despachador.publicar_comando_revertir_validacion(evento, 'comando_revertir_validacion')
        

    