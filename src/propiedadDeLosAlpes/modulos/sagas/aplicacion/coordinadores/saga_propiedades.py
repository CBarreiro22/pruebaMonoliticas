from propiedadDeLosAlpes.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin

from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.cancelar_creacion_propiedad import CancelarPropiedad as CancelarCreacionPropiedad
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.validar_propiedad import ValidarPropiedad
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.enriquecer_propiedad import EnriquecerPropiedad
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.habilitar_propiedad import HabilitarPropiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.eventos import PropiedadCreada, PropiedadHabilitada  
from propiedadDeLosAlpes.modulos.auditoria.dominio.eventos import EventoPropiedadValidada, ValidacionPropiedadFallida
from propiedadDeLosAlpes.modulos.agente.dominio.eventos import PropiedadEnriquecida

from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.seedwork.dominio.eventos import EventoDominio
from propiedadDeLosAlpes.modulos.sagas.dominio.eventos.propiedades import CreacionPropiedadFallida, EnriquecimientoPropiedadFallida, HabilitacionPropiedadFallida
from propiedadDeLosAlpes.modulos.auditoria.dominio.comandos import RevertirEnriquecimientoPropiedad
from propiedadDeLosAlpes.modulos.agente.dominio.comando import RevertirValidacionPropiedad
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando
from propiedadDeLosAlpes.seedwork.aplicacion.handlers import Handler




class CoordinadorPropiedades(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearPropiedad, evento=PropiedadCreada, error=CreacionPropiedadFallida, compensacion=CancelarCreacionPropiedad),
            Transaccion(index=2, comando=ValidarPropiedad, evento=EventoPropiedadValidada, error=ValidacionPropiedadFallida, compensacion=RevertirValidacionPropiedad),
            Transaccion(index=3, comando=EnriquecerPropiedad, evento=PropiedadEnriquecida, error=EnriquecimientoPropiedadFallida, compensacion=RevertirEnriquecimientoPropiedad),
            Transaccion(index=4, comando=HabilitarPropiedad, evento=PropiedadHabilitada, error=HabilitacionPropiedadFallida, compensacion=RevertirEnriquecimientoPropiedad),
            Fin(index=5)
        ]

    def iniciar(self):
        print("*********** Inicio SAGA")
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        print("*********** Fin SAGA")
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        
        #from propiedadDeLosAlpes.modulos.sagas.dominio.repositorios import RepositorioSaga

        #saga: Saga = Agente(id_propiedad=id_propiedad,  propiedades_completadas=diccionario_string)
        #fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        
        #repositorio = self.fabrica_repositorio.crear_objeto (RepositorioSaga.__class__)
        #repositorio.agregar(saga)
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        
        #EVENTOS EXITOSOS
        if evento.__class__ == PropiedadCreada:
            comando = ValidarPropiedad(id_propiedad = str(evento.id_propiedad))

        if evento.__class__ == EventoPropiedadValidada:
            comando = EnriquecerPropiedad(id_propiedad = str(evento.id_propiedad), campos_faltantes= evento.campos_faltantes)

        if evento.__class__ == PropiedadEnriquecida:
             comando = HabilitarPropiedad(id_propiedad = str(evento.id_propiedad), propiedades_completadas=evento.propiedades_completadas )

        #EVENTOS FALLIDOS
        if evento.__class__ == ValidacionPropiedadFallida:
             comando = CancelarCreacionPropiedad(id_propiedad = str(evento.id_propiedad) )

        if evento.__class__ == EnriquecimientoPropiedadFallida:
             comando = RevertirValidacionPropiedad(id_propiedad = str(evento.id_propiedad) )
            
        if evento.__class__ == HabilitacionPropiedadFallida:
             comando = RevertirEnriquecimientoPropiedad(id_propiedad = str(evento.id_propiedad) )

        return comando

    def publicar_comando(self, evento: EventoDominio, tipo_comando: type):
        comando = self.construir_comando(evento, tipo_comando)
        ejecutar_commando(comando)

    def __init__(self):
        self.inicializar_pasos()

class HandlerSaga(Handler):
    @staticmethod    
    def oir_mensaje(evento):
        if isinstance(evento, EventoDominio):
            coordinador = CoordinadorPropiedades()
            coordinador.procesar_evento(evento)
        else:
            raise NotImplementedError("El mensaje no es evento de Dominio")
