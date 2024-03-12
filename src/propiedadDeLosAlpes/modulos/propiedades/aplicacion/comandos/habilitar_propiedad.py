from dataclasses import dataclass
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.base import CrearPropiedadBaseHandler
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.eventos import PropiedadHabilitada
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from propiedadDeLosAlpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from propiedadDeLosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
import json
from pydispatch import dispatcher

@dataclass
class HabilitarPropiedad (Comando):
    id_propiedad: str
    propiedades_completadas: str

class HabilitarPropiedadHandler (CrearPropiedadBaseHandler) :

    def handle(self, comando: HabilitarPropiedad):
        print(f"============= SAGAS - Comando para Propiedad: Habilitar Propiedad - mensaje: {comando}")

        datos = json.loads(comando.propiedades_completadas)
        propiedad: Propiedad = Propiedad(
            id_propietario = comando.id_propiedad,  
            nombre_propietario = datos.get("nombre_propietario"),
            direccion = datos.get("direccion"),
            pais = datos.get("pais"),
            tipo_propiedad = datos.get("tipo_propiedad"),
            ubicacion = datos.get("ubicacion"),
            id_empresa = datos.get("id_empresa"),
            superficie = datos.get("superficie"),
            precio = datos.get("precio"),
            estado = "exitoso"
        )
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        repositorio.actualizar(propiedad)

        #UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, propiedad)
        #UnidadTrabajoPuerto.savepoint()
        #UnidadTrabajoPuerto.commit()

        propiedad_habilitada = PropiedadHabilitada(id_propiedad=comando.id_propiedad)
        dispatcher.send(signal=f'{type(propiedad_habilitada).__name__}Dominio', evento=propiedad_habilitada)
    

@comando.register(HabilitarPropiedad)
def ejecutar_comando_habilitar_propiedad(comando:HabilitarPropiedad):
    handler = HabilitarPropiedadHandler()
    handler.handle(comando)



