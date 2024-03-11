from dataclasses import dataclass
from propiedadDeLosAlpes.modulos.auditoria.aplicacion.comandos.base import AuditoriaBaseHandler
#from propiedadDeLosAlpes.modulos.auditoria.aplicacion.mapeadores import MapeadorAuditoria
from propiedadDeLosAlpes.modulos.auditoria.dominio.entidades import Auditoria
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from propiedadDeLosAlpes.modulos.auditoria.dominio.repositorios import RepositorioAuditoria
from propiedadDeLosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.adaptadores import ServicioExternoPropiedades




@dataclass
class ValidarPropiedad (Comando):
    id_propiedad: str

class ValidarPropiedadHandler (AuditoriaBaseHandler) :

    def handle(self, comando: ValidarPropiedad):
        print("Guarda en auditoria")
        print("publica evento propiedad validad")
        print(comando)

        id_propiedad = comando.id_propiedad

        #servicio_propiedades = ServicioExternoPropiedades()
        #auditoria_propiedad_dict=servicio_propiedades.obtener_datos(id_propiedad=id_propiedad)
        # map_auditoria = MapeadorAuditoriaDTOJson()
        # auditoria_propiedad_dto = map_auditoria.externo_a_dto(auditoria_propiedad_dict)
        # fabrica_auditoria = FabricaAuditoria()
        
        #auditoria: Auditoria = fabrica_auditoria.crear_objeto(auditoria_propiedad_dto, MapeadorAuditoria())
        auditoria:Auditoria = Auditoria(id_propiedad=comando.id_propiedad)
        auditoria.validar_propiedad(auditoria)

        # # propiedad_dto = PropiedadDTO(
        # #     direccion=comando.direccion,
        # #     pais=comando.pais,
        # #     tipo_propiedad=comando.tipo_propiedad,
        # #     nombre_propietario=comando.nombre_propietario,
        # #     ubicacion=comando.ubicacion,
        # #     id_empresa=comando.id_empresa,
        # #     superficie=comando.superficie,
        # #     precio=comando.precio,
        # #     estado=comando.estado
        # # )

        # # propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        # # propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto (RepositorioAuditoria.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, auditoria)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(ValidarPropiedad)
def ejecutar_comando_validar_propiedad(comando:ValidarPropiedad):
    handler = ValidarPropiedadHandler()
    handler.handle(comando)



