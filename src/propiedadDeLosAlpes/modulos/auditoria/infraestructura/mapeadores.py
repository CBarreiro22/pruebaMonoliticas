
from propiedadDeLosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadDeLosAlpes.modulos.auditoria.dominio.entidades import Auditoria
from .dto import AuditoriaDTO


class MapeadorAuditoriaDTOJson(AppMap):
    def externo_a_dto(self, datos: dict) -> AuditoriaDTO:
        auditoria_dto = AuditoriaDTO()
        auditoria_dto.id_propiedad = datos['id_propiedad']
        auditoria_dto.direccion= datos['direccion']
        auditoria_dto.pais = datos['pais']
        auditoria_dto.tipo_propiedad = datos['tipo_propiedad']
        auditoria_dto.ubicacion = datos['ubicacion']    
        auditoria_dto.precio = datos['precio']  
        auditoria_dto.id_empresa = datos['id_empresa']
        auditoria_dto.superficie = datos['superficie']  
        auditoria_dto.estado = datos['estado']
        return auditoria_dto

    def dto_a_externo(self, dto: AuditoriaDTO) -> dict:
        return dto.__dict__
    
class MapeadorAuditoria(RepMap):
    def obtener_tipo(self) -> type:
        return Auditoria.__class__
    
    def entidad_a_dto(self, entidad: Auditoria) -> AuditoriaDTO:
        return AuditoriaDTO(id_propiedad=entidad.id_propiedad, direccion=entidad.direccion, pais=entidad.pais, tipo_propiedad=entidad.tipo_propiedad, ubicacion=entidad.ubicacion, precio=entidad.precio, id_empresa=entidad.id_empresa, superficie=entidad.superficie, estado=entidad.estado)

    def dto_a_entidad(self, dto: AuditoriaDTO) -> Auditoria:
        auditoria= Auditoria()
        auditoria.id_propiedad = dto.id_propiedad
        auditoria.direccion= dto.direccion
        auditoria.pais = dto.pais
        auditoria.tipo_propiedad = dto.tipo_propiedad
        auditoria.ubicacion = dto.ubicacion
        auditoria.precio = dto.precio
        auditoria.id_empresa = dto.id_empresa
        auditoria.superficie = dto.superficie
        auditoria.estado = dto.estado
        return auditoria