from dataclasses import dataclass
from propiedadDeLosAlpes.modulos.agente.aplicacion.comandos.base import AgenteBaseHandler
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedadDeLosAlpes.modulos.agente.dominio.entidades import Agente
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from propiedadDeLosAlpes.modulos.agente.dominio.repositorios import RepositorioAgente
from propiedadDeLosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedadDeLosAlpes.modulos.agente.infraestructura.fabricas import FabricaRepositorio
from propiedadDeLosAlpes.modulos.agente.dominio.eventos import PropiedadEnriquecida
from pydispatch import dispatcher
import random, json
from faker import Faker

faker = Faker()

@dataclass
class EnriquecerPropiedad (Comando):
    id_propiedad: str
    campos_faltantes: str

class EnriquecerPropiedadHandler (AgenteBaseHandler) :

    def handle(self, comando: EnriquecerPropiedad):
        print(f"============= SAGAS - Comando para Agente: Enriquecer Propiedad - mensaje: {comando}")

        id_propiedad = comando.id_propiedad 
        lista_campos = comando.campos_faltantes  
        print(comando)
        diccionario = {}
        for campo in lista_campos:
            diccionario[campo] = bot_simula_proceso_completar_campos(campo)

        diccionario_string = json.dumps(diccionario)
        agente: Agente = Agente(id_propiedad=id_propiedad,  propiedades_completadas=diccionario_string)
        agente.crear_agente_propiedad(agente)
        
        fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        repositorio = self.fabrica_repositorio.crear_objeto (RepositorioAgente.__class__)
        repositorio.agregar(agente)

        propiedad_enriquecida = PropiedadEnriquecida(id_propiedad=id_propiedad,  propiedades_completadas=diccionario_string)
        dispatcher.send(signal=f'{type(propiedad_enriquecida).__name__}Dominio', evento=propiedad_enriquecida)
    
   

        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, agente)
        #UnidadTrabajoPuerto.savepoint()
        #UnidadTrabajoPuerto.commit()

       

       
        # fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        # repositorio = fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        #repositorio.actualizar(propiedad)

        # propiedad_dto = PropiedadDTO(
        #     id_propiedad=comando.id_propiedad,
        #     pais=comando.pais,
        #     tipo_propiedad=comando.tipo_propiedad,
        #     nombre_propietario=comando.nombre_propietario,
        #     ubicacion=comando.ubicacion,
        #     id_empresa=comando.id_empresa,
        #     superficie=comando.superficie,
        #     precio=comando.precio,
        #     estado=comando.estado
        # )

        # propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        # propiedad.crear_propiedad(propiedad)

        # repositorio = self.fabrica_repositorio.crear_objeto (RepositorioPropiedades.__class__)

        # UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, propiedad)
        # UnidadTrabajoPuerto.savepoint()
        # UnidadTrabajoPuerto.commit()

def bot_simula_proceso_completar_campos(campo):
        if campo == "nombre_propietario":
            return faker.name()

        if campo == "direccion":
            return faker.address()

        if campo == "pais":
            return faker.country()

        if campo == "tipo_propiedad":
            return "Casa"

        if campo == "ubicacion":
            return faker.address()

        if campo == "id_empresa":
            return 123

        if campo == "superficie":
            return round(random.uniform(50, 200), 2)

        if campo == "precio":
            return random.randint(100000000, 500000000)



@comando.register(EnriquecerPropiedad)
def ejecutar_comando_enriquecer_propiedad(comando:EnriquecerPropiedad):
    handler = EnriquecerPropiedadHandler()
    handler.handle(comando)



