from propiedadDeLosAlpes.seedwork.aplicacion.handlers import Handler
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerPropiedadDominio(Handler):

    # @staticmethod
    # def handle_propiedad_creada(evento):
    #     despachador = Despachador()
    #     despachador.publicar_evento(evento, 'eventos-propiedad-modificada')
    
    # @staticmethod
    # def handle_propiedad_validacion_agente(evento):
    #     despachador = Despachador()
    #     despachador.publicar_evento_agente(evento, 'eventos-propiedad-registrada')

    #Nuevos
    @staticmethod
    def handle_comando_validar_propiedad(evento):
        despachador = Despachador()
        despachador.publicar_comando_validar_propiedad(evento, 'comando-validar-propiedad')
    
    @staticmethod
    def handle_comando_enriquecer_propiedad(evento):
        despachador = Despachador()
        despachador.publicar_comando_enriquecer_propiedad(evento, 'comando-enriquecer-propiedad')
    
    @staticmethod
    def handle_comando_revertir_enriquecimiento(evento):
        despachador = Despachador()
        despachador.publicar_comando_revertir_enriquecimiento(evento, 'comando-revertir-enriquecimiento')

    @staticmethod
    def handle_evento_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento_propiedad_creada(evento, 'evento-propiedad-creada')
    
    @staticmethod
    def handle_evento_propiedad_habilitada(evento):
        despachador = Despachador()
        despachador.publicar_evento_propiedad_habilitada(evento, 'evento-propiedad-habilitada')

        