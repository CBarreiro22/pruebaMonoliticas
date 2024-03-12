from dataclasses import dataclass
from propiedadDeLosAlpes.modulos.auditoria.aplicacion.comandos.base import AuditoriaBaseHandler
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.mapeadores import MapeadorAuditoriaDTOJson, MapeadorAuditoria
from propiedadDeLosAlpes.modulos.auditoria.dominio.entidades import Auditoria
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from propiedadDeLosAlpes.modulos.auditoria.dominio.repositorios import RepositorioAuditoria
from propiedadDeLosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedadDeLosAlpes.modulos.auditoria.infraestructura.adaptadores import ServicioExternoPropiedades
from pydispatch import dispatcher
from propiedadDeLosAlpes.modulos.auditoria.dominio.eventos import EventoPropiedadValidada, ValidacionPropiedadFallida

@dataclass
class ValidarPropiedad (Comando):
    id_propiedad: str

class ValidarPropiedadHandler (AuditoriaBaseHandler) :

    def handle(self, comando: ValidarPropiedad):
        print(f"============= SAGAS - Comando para Auditoria: Validar Propiedad - mensaje: {comando}")
        try:

            #div =1/0

            servicio_propiedades = ServicioExternoPropiedades()
            auditoria_propiedad_dict=servicio_propiedades.obtener_datos(id_propiedad=comando.id_propiedad)
            map_auditoria = MapeadorAuditoriaDTOJson()
            auditoria_propiedad_dto = map_auditoria.externo_a_dto(auditoria_propiedad_dict)
            auditoria: Auditoria = self.fabrica_auditoria.crear_objeto(auditoria_propiedad_dto, MapeadorAuditoria())
            auditoria:Auditoria = Auditoria(
                id_propiedad=comando.id_propiedad,
                nombre_propietario=auditoria.nombre_propietario,
                direccion=auditoria.direccion,
                pais=auditoria.pais,
                tipo_propiedad=auditoria.tipo_propiedad,
                ubicacion=auditoria.ubicacion,
                precio=auditoria.precio,
                id_empresa=auditoria.id_empresa,
                superficie=auditoria.superficie,
            )

            validacion = auditoria.validar_propiedad(auditoria)
            repositorio = self.fabrica_repositorio.crear_objeto (RepositorioAuditoria.__class__)
            
            propiedad_validada = EventoPropiedadValidada(id_propiedad=comando.id_propiedad,estado=validacion.estado,  campos_faltantes=validacion.campos_faltantes)
            dispatcher.send(signal=f'{type(propiedad_validada).__name__}Dominio', evento=propiedad_validada)
        
            #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, auditoria)
            #UnidadTrabajoPuerto.savepoint()
            #UnidadTrabajoPuerto.commit()
        except Exception as e:
            mensaje = f"Error al validar la propiedad: {e}"
            evento = ValidacionPropiedadFallida(id_propiedad=comando.id_propiedad, mensaje=mensaje)
            dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
        

@comando.register(ValidarPropiedad)
def ejecutar_comando_validar_propiedad(comando:ValidarPropiedad):
    handler = ValidarPropiedadHandler()
    handler.handle(comando)



