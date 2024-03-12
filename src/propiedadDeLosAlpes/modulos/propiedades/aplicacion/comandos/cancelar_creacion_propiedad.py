from dataclasses import dataclass
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.base import CrearPropiedadBaseHandler
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from propiedadDeLosAlpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from propiedadDeLosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from pydispatch import dispatcher

@dataclass
class CancelarPropiedad (Comando):
    id_propiedad: str

class CancelarPropiedadHandler (CrearPropiedadBaseHandler) :

    def handle(self, comando: CancelarPropiedad):
        print(f"============= SAGAS - Comando para Cancelar Propiedad: Cancelar Propiedad - mensaje: {comando}")
        
        # propiedad_dto = PropiedadDTO(
        #     direccion=comando.direccion,
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


        #fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        
        repositorio = self.fabrica_repositorio.crear_objeto (RepositorioPropiedades.__class__)
        repositorio.eliminar(comando.id_propiedad)


        from propiedadDeLosAlpes.modulos.agente.dominio.eventos import PropiedadNoCreada
        evento = PropiedadNoCreada(id_propiedad=comando.id_propiedad)
        dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
    

        # UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, data.id_propiedad)
        # UnidadTrabajoPuerto.savepoint()
        # UnidadTrabajoPuerto.commit()

@comando.register(CancelarPropiedad)
def ejecutar_comando_cancelar_propiedad(comando:CancelarPropiedad):
    handler = CancelarPropiedadHandler()
    handler.handle(comando)



