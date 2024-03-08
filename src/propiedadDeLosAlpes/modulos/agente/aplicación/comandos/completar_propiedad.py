from dataclasses import dataclass
from propiedadDeLosAlpes.modulos.agente.aplicación.comandos.base import CompletarPropiedadBaseHandler
from propiedadDeLosAlpes.modulos.agente.aplicación.dto import PropiedadCompletadaDTO
from propiedadDeLosAlpes.modulos.agente.aplicación.mapeadores import MapeadorPropiedadCompletada
from propiedadDeLosAlpes.modulos.agente.dominio.entidades import PropiedadCompletada
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from propiedadDeLosAlpes.modulos.agente.dominio.repositorios import RepositorioPropiedadesCompletadas
from propiedadDeLosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from typing import Dict


@dataclass
class CompletarPropiedad (Comando):
    id: str
    campos_faltantes: str

class CompletarPropiedadHandler (CompletarPropiedadBaseHandler) :

    def handle(self, comando: CompletarPropiedad):
        print(f'Comando handle CompletarPropiedadHandler: {comando}')
        propiedad_completada_dto = PropiedadCompletadaDTO(
            id=comando.id,
            campos_faltantes=comando.campos_faltantes
        )
        print(f'propiedad_completada_dto: {propiedad_completada_dto}')

        propiedad_completada: PropiedadCompletada = self.fabrica_propiedades.crear_objeto(propiedad_completada_dto, MapeadorPropiedadCompletada())
        propiedad_completada.crear_propiedad_completada(propiedad_completada)

        print('propiedad_completada.crear_propiedad_completada(propiedad_completada)')

        repositorio = self.fabrica_repositorio.crear_objeto (RepositorioPropiedadesCompletadas.__class__)

        print('self.fabrica_repositorio.crear_objeto')
        print(propiedad_completada)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad_completada)

        print('UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad_completada)')
        
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(CompletarPropiedad)
def ejecutar_comando_completar_propiedad(comando:CompletarPropiedad):
    print(f'Comando recibido ejecutar_comando_completar_propiedad: {comando}')
    handler = CompletarPropiedadHandler()
    handler.handle(comando)



