from propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedadDeLosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadDeLosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadDeLosAlpes.seedwork.dominio.entidades import Entidad
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap


class MapeadorPropiedadDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO(
            tipo_propiedad=externo['tipo_propiedad'], 
            direccion=externo['direccion'], 
            pais=externo['pais'], 
            nombre_propietario=externo['nombre_propietario'],
            id_empresa=externo['id_empresa'],
            superficie=externo['superficie'],
            precio=externo['precio'],
            ubicacion=externo['ubicacion'])
        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__


class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Entidad) -> PropiedadDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)

        return PropiedadDTO(
            fecha_creacion=fecha_creacion, 
            fecha_actualizacion=fecha_actualizacion, 
            id=_id,
            tipo_propiedad=entidad.tipo_propiedad,
            direccion=entidad.direccion,
            pais=entidad.pais,
            nombre_propietario=entidad.nombre_propietario,
            id_empresa=entidad.id_empresa,
            superficie=entidad.superficie,
            precio=entidad.precio,
            estado=entidad.estado,
            ubicacion=entidad.ubicacion
        )

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(
            direccion=dto.direccion, 
            pais=dto.pais, 
            tipo_propiedad=dto.tipo_propiedad, 
            nombre_propietario=dto.nombre_propietario,
            id_empresa=dto.id_empresa,
            superficie=dto.superficie,
            precio=dto.precio,
            estado=dto.estado,
            ubicacion=dto.ubicacion        
        )
        return propiedad
