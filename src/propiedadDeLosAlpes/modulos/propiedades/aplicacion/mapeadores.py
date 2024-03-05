from propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedadDeLosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadDeLosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadDeLosAlpes.seedwork.dominio.entidades import Entidad
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap


class MapeadorPropiedadDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        #propiedad_dto = PropiedadDTO()
          
    
    
    
    
    #, ubicacion= externo['ubicacion']
    #, id_empresa=externo['id_empresa']
    # "superficie": 1.1,
    # "precio":23.2,
    # "estado": "Bogota",
    # "fecha_actualizacion": "12-12-24",
    # "fecha_creacion": "12-12-24"
        propiedad_dto = PropiedadDTO(tipo_propiedad=externo['tipo_propiedad']
                                        , direccion=externo['direccion']
                                        , pais=externo['pais']
                                        , nombre_propietario=externo['nombre_propietario']
                                        , fecha_creacion=externo['fecha_creacion']
                                        , fecha_actualizacion=externo['fecha_actualizacion']
                                       
                                       
                                        )

        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__


class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Entidad) -> any:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)

        return PropiedadDTO(fecha_creacion=fecha_creacion, fecha_actualizacion=fecha_actualizacion, id=_id)

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(direccion=dto.direccion, pais=dto.pais, tipo_propiedad=dto.tipo_propiedad, nombre_propietario=dto.nombre_propietario
        #,fecha_creacion=dto.fecha_creacion, fecha_actualizacion=dto.fecha_actualizacion
        )
        return propiedad
