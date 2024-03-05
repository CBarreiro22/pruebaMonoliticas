
from propiedadDeLosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadDeLosAlpes.modulos.auditoria.dominio.entidades import Auditoria
from .dto import AuditoriaDTO


class MapeadorAuditoriaDTOJson(AppMap):
    def externo_a_dto(self, datos: dict) -> AuditoriaDTO:
        return AuditoriaDTO(id_propiedad=datos['id'], direccion=datos.get('direccion'), pais=datos.get('pais'), tipo_propiedad=datos.get('tipo_propiedad'), ubicacion=datos.get('ubicacion'), precio=datos.get('precio'), id_empresa=datos.get('id_empresa'), superficie=datos.get('superficie'), estado=datos.get('estado'))

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