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
        return Propiedad(
            id=dto.id, 
            fecha_creacion=dto.fecha_creacion, 
            fecha_actualizacion=dto.fecha_actualizacion, 
            nombre_propietario=dto.nombre_propietario, 
            direccion=dto.direccion, 
            pais=dto.pais, 
            tipo_propiedad=dto.tipo_propiedad, 
            ubicacion=dto.ubicacion, 
            precio=dto.precio, 
            id_empresa=dto.id_empresa, 
            superficie=dto.superficie, 
            estado=dto.estado
        )
