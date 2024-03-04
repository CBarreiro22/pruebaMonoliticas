""" Mapeadores para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador
from propiedadDeLosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO


class MapeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        propiedad_dto.id = str(entidad.id)
        propiedad_dto.nombre_propietario=entidad.nombre_propietario
        propiedad_dto.direccion=entidad.direccion
        propiedad_dto.pais=entidad.pais
        propiedad_dto.tipo_propiedad=entidad.tipo_propiedad
        propiedad_dto.ubicacion=entidad.ubicacion
        propiedad_dto.precio=entidad.precio
        propiedad_dto.id_empresa=entidad.id_empresa
        propiedad_dto.superficie=entidad.superficie
        propiedad_dto.estado=entidad.estado
        propiedad_dto.fecha_creacion = entidad.fecha_creacion
        propiedad_dto.fecha_actualizacion = entidad.fecha_actualizacion
        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)

        return propiedad
