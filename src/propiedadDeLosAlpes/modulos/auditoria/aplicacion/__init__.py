from pydispatch import dispatcher
from .handlers import HandlerAuditoriaDominio

#dispatcher.connect(HandlerAuditoriaDominio.handle_propiedad_modificada, signal='ResultadosValidacionDominio')

dispatcher.connect(HandlerAuditoriaDominio.handle_evento_propiedad_validada, signal='EventoPropiedadValidadaDominio')
dispatcher.connect(HandlerAuditoriaDominio.handle_comando_cancelar_creacion_propiedad, signal='CancelarCreacionPropiedadDominio')

