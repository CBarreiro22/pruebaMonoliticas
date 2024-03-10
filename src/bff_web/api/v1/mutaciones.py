import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    # TODO Agregue objeto de itinerarios o reserva
    @strawberry.mutation
    async def registrar_propiedad(self, nombre_propietario: str, direccion: str, pais: str, tipo_propiedad: str, ubicacion: str, id_empresa: int, superficie: float, precio: float, info: Info) -> RegistrarPropiedadRespuesta:
        print(f"Nombre Pripetario: {nombre_propietario}, Dirección: {direccion}, Pais: {pais}, Tipo propiedad: {tipo_propiedad}, Ubicación: {ubicacion}, Id Empresa: {id_empresa}, Superficie: {superficie}, Precio {precio}")
        payload = dict(
            nombre_propietario = nombre_propietario,
            direccion = direccion,
            pais = pais,
            tipo_propiedad = tipo_propiedad,
            ubicacion = ubicacion, 
            id_empresa = id_empresa,
            superficie = superficie,
            precio = precio
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoRegistrarPropiedad",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-crear-propiedad", "public/default/comando-crear-reserva")
        
        return RegistrarPropiedadRespuesta(mensaje="Procesando Mensaje", codigo=203)