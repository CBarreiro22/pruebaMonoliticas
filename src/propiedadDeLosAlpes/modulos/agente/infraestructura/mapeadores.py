""" Mapeadores para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador
from propiedadDeLosAlpes.modulos.agente.dominio.entidades import Agente
from .dto import Agente as AgenteDTO


class MapeadorAgente(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Agente.__class__

    def entidad_a_dto(self, entidad: Agente) -> AgenteDTO:
        agente_dto = AgenteDTO()
        agente_dto.id = str(entidad.id)
        agente_dto.id_propiedad=entidad.id_propiedad
        agente_dto.propiedades_completadas=entidad.propiedades_completadas
        return agente_dto

    def dto_a_entidad(self, dto: AgenteDTO) -> Agente:
        return Agente(
            id=dto.id, 
            id_propiedad=dto.id_propiedad, 
            propiedades_completadas=dto.propiedades_completadas
        )
