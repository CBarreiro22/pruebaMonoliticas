from pydispatch import dispatcher
from .handlers import HandlerPropiedadCreadaDominio

dispatcher.connect(HandlerPropiedadCreadaDominio.handle_propiedad_creada, signal='PropiedadCreadaDominio')
