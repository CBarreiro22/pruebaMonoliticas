from pydispatch import dispatcher
from src.propiedadDeLosAlpes.modulos.sagas.aplicacion.coordinadores.saga_propiedades import oir_mensaje

#dispatcher.connect(HandlerPropiedadDominio.handle_evento_propiedad_creada, signal='PropiedadCreadaDominio')
dispatcher.connect(oir_mensaje, signal='PropiedadCreadaDominio')