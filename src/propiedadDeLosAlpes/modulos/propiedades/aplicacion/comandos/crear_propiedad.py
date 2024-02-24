from dataclasses import dataclass
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.base import CrearPropiedadBaseHandler
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO


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
        propiedad_dto = PropiedadDTO(
            direccion=comando.direccion,
            pais=comando.pais,
            tipo_propiedad=comando.tipo_propiedad,
            nombre_propietario=comando.nombre_propietario,
            id=comando.id,
            fecha_creacion=comando.fecha_creacion,
            fecha_actualizacion=comando.fecha_actualizacion
        )

        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto (RepositorioPropiedades.__class__)


