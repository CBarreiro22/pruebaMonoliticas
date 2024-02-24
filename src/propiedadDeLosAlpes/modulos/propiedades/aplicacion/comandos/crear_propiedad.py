from dataclasses import dataclass

from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.base import CrearPropiedadBaseHandler



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

    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDto(
            direccion=comando.direccion,
            pais=comando.pais,
            tipo_propiedad=comando.tipo_propiedad,
            nombre_propietario=comando.nombre_propietario,
            id=comando.id,
            fecha_creacion=comando.fecha_creacion,
            fecha_actualizacion=comando.fecha_actualizacion
        )

        propiedad: Propiedad
