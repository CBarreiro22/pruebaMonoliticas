from pydispatch import dispatcher
from .handlers import HandlerPropiedadCreadaDominio

dispatcher.connect(HandlerPropiedadCreadaDominio.handle_propiedad_creada, signal='PropiedadCreadaDominio')
dispatcher.connect(HandlerPropiedadCreadaDominio.handle_propiedad_validacion_agente, signal='ResultadosValidacionAgenteDominio')
