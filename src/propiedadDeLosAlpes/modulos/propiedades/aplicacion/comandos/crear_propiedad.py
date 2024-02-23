from dataclasses import dataclass

from src.propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando


@dataclass
class CrearPropiedad (Comando):
    direccion: str
    pais: str
    tipo_propiedad: str
    nombre_propietario: str
    id: str
    fecha_creacion: str
    fecha_actualizacion: str


class CrearPropiedadHandler (CrearPropiedadBaseHandler) :
