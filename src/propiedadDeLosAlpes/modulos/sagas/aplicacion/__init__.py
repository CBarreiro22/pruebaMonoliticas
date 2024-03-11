from pydispatch import dispatcher
from propiedadDeLosAlpes.modulos.sagas.aplicacion.coordinadores.saga_propiedades import HandlerSaga

#dispatcher.connect(HandlerPropiedadDominio.handle_evento_propiedad_creada, signal='PropiedadCreadaDominio')
dispatcher.connect(HandlerSaga.oir_mensaje, signal='PropiedadCreadaDominio')
dispatcher.connect(HandlerSaga.oir_mensaje, signal='OirMensaje')
