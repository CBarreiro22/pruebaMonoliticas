from pydispatch import dispatcher
from .handlers import HandlerPropiedadDominio

#dispatcher.connect(HandlerPropiedadDominio.handle_propiedad_creada, signal='PropiedadCreadaDominio')
#dispatcher.connect(HandlerPropiedadDominio.handle_propiedad_validacion_agente, signal='ResultadosValidacionAgenteDominio')

dispatcher.connect(HandlerPropiedadDominio.handle_comando_validar_propiedad, signal='ComandoValidarPropiedadDominio')
dispatcher.connect(HandlerPropiedadDominio.handle_comando_enriquecer_propiedad, signal='EnriquecerPropiedadDominio')
dispatcher.connect(HandlerPropiedadDominio.handle_comando_revertir_enriquecimiento, signal='RevertirEnriquecimientoPropiedadDominio')
dispatcher.connect(HandlerPropiedadDominio.handle_evento_propiedad_creada, signal='PropiedadCreadaDominio')
