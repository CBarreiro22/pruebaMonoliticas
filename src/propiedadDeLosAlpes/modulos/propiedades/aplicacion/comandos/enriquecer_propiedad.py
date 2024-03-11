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
class EnriquecerPropiedad (Comando):
    id_propiedad: str

class EnriquecerPropiedadHandler (CrearPropiedadBaseHandler) :

    def handle(self, comando: EnriquecerPropiedad):
        print("Guarda en agente")
        print("publica evento propiedad enriquecida")
        # propiedad_dto = PropiedadDTO(
        #     id_propiedad=comando.id_propiedad,
        #     pais=comando.pais,
        #     tipo_propiedad=comando.tipo_propiedad,
        #     nombre_propietario=comando.nombre_propietario,
        #     ubicacion=comando.ubicacion,
        #     id_empresa=comando.id_empresa,
        #     superficie=comando.superficie,
        #     precio=comando.precio,
        #     estado=comando.estado
        # )

        # propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        # propiedad.crear_propiedad(propiedad)

        # repositorio = self.fabrica_repositorio.crear_objeto (RepositorioPropiedades.__class__)

        # UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        # UnidadTrabajoPuerto.savepoint()
        # UnidadTrabajoPuerto.commit()

@comando.register(EnriquecerPropiedad)
def ejecutar_comando_enriquecer_propiedad(comando:EnriquecerPropiedad):
    handler = EnriquecerPropiedadHandler()
    handler.handle(comando)



