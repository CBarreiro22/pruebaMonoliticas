from pydispatch import dispatcher
from src.propiedadDeLosAlpes.modulos.sagas.aplicacion.coordinadores.saga_propiedades import oir_mensaje

dispatcher.connect(oir_mensaje, signal='OirMensajeSaga')