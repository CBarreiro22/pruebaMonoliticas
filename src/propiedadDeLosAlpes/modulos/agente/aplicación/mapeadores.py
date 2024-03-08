from propiedadDeLosAlpes.modulos.agente.aplicación.dto import PropiedadCompletadaDTO
from propiedadDeLosAlpes.modulos.agente.dominio.entidades import PropiedadCompletada
from propiedadDeLosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadDeLosAlpes.seedwork.dominio.entidades import Entidad
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap


# class MapeadorPropiedadDTOJson(AppMap):

#     def externo_a_dto(self, externo: dict) -> PropiedadCompletadaDTO:
#         propiedad_completada_dto = PropiedadCompletadaDTO(
#             tipo_propiedad=externo['tipo_propiedad'], 
#             direccion=externo['direccion'], 
#             pais=externo['pais'], 
#             nombre_propietario=externo['nombre_propietario'],
#             id_empresa=externo['id_empresa'],
#             superficie=externo['superficie'],
#             precio=externo['precio'],
#             ubicacion=externo['ubicacion'])
#         return propiedad_completada_dto

#     def dto_a_externo(self, dto: PropiedadCompletadaDTO) -> dict:
#         return dto.__dict__


class MapeadorPropiedadCompletada(RepMap):

    def obtener_tipo(self) -> type:
        return PropiedadCompletada.__class__

    def entidad_a_dto(self, entidad: Entidad) -> PropiedadCompletadaDTO:
        _id = str(entidad.id)
        return PropiedadCompletadaDTO(
            id=_id,
            campos_faltantes=entidad.campos_faltantes
        )

    def dto_a_entidad(self, dto: PropiedadCompletadaDTO) -> PropiedadCompletada:
        propiedad = PropiedadCompletada(
            id=dto.id, 
            campos_faltantes=dto.campos_faltantes  
        )
        return propiedad
