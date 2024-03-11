from dataclasses import dataclass
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.base import CrearPropiedadBaseHandler
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from propiedadDeLosAlpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from propiedadDeLosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto


@dataclass
class CrearPropiedad (Comando):
    direccion: str
    pais: str
    tipo_propiedad: str
    nombre_propietario: str
    ubicacion: str
    id_empresa: int
    superficie: float
    precio: float
    estado: str

class CrearPropiedadHandler (CrearPropiedadBaseHandler) :

    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
            direccion=comando.direccion,
            pais=comando.pais,
            tipo_propiedad=comando.tipo_propiedad,
            nombre_propietario=comando.nombre_propietario,
            ubicacion=comando.ubicacion,
            id_empresa=comando.id_empresa,
            superficie=comando.superficie,
            precio=comando.precio,
            estado=comando.estado
        )

        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto (RepositorioPropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando:CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)



