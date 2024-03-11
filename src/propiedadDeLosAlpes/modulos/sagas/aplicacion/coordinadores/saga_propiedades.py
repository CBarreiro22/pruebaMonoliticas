from propiedadDeLosAlpes.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin

from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.validar_propiedad import ValidarPropiedad
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.enriquecer_propiedad import EnriquecerPropiedad
#from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.habilitar_propiedad import HabilitarPropiedad


from propiedadDeLosAlpes.modulos.propiedades.dominio.eventos import PropiedadCreada  
from propiedadDeLosAlpes.modulos.auditoria.dominio.eventos import EventoPropiedadValidada
from propiedadDeLosAlpes.modulos.agente.dominio.eventos import PropiedadEnriquecida


from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.seedwork.dominio.eventos import EventoDominio

from propiedadDeLosAlpes.modulos.sagas.dominio.eventos.propiedades import CreacionPropiedadFallida, ValidacionPropiedadFallida, EnriquecimientoPropiedadFallida, HabilitacionPropiedadFallida

#Comandos
from propiedadDeLosAlpes.modulos.auditoria.dominio.comandos import CancelarCreacionPropiedad, RevertirEnriquecimientoPropiedad
from propiedadDeLosAlpes.modulos.agente.dominio.comando import RevertirValidacionPropiedad

from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando


# from aeroalpes.modulos.sagas.aplicacion.comandos.propiedades import RegistrarUsuario, ValidarUsuario
# from aeroalpes.modulos.sagas.aplicacion.comandos.auditoria import PagarReserva, RevertirPago
# from aeroalpes.modulos.sagas.aplicacion.comandos.agente import ConfirmarReserva, RevertirConfirmacion

# from aeroalpes.modulos.vuelos.aplicacion.comandos.crear_reserva import CrearReserva
# from aeroalpes.modulos.vuelos.aplicacion.comandos.aprobar_reserva import AprobarReserva
# from aeroalpes.modulos.vuelos.aplicacion.comandos.cancelar_reserva import CancelarReserva
# from aeroalpes.modulos.vuelos.dominio.eventos.reservas import ReservaCreada, ReservaCancelada, ReservaAprobada, CreacionReservaFallida, AprobacionReservaFallida
# from aeroalpes.modulos.sagas.dominio.eventos.pagos import ReservaPagada, PagoRevertido
# from aeroalpes.modulos.sagas.dominio.eventos.gds import ReservaGDSConfirmada, ConfirmacionGDSRevertida, ConfirmacionFallida


class CoordinadorPropiedades(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearPropiedad, evento=PropiedadCreada, error=CreacionPropiedadFallida, compensacion=CancelarCreacionPropiedad),
            Transaccion(index=2, comando=ValidarPropiedad, evento=EventoPropiedadValidada, error=ValidacionPropiedadFallida, compensacion=RevertirValidacionPropiedad),
            Transaccion(index=3, comando=EnriquecerPropiedad, evento=PropiedadEnriquecida, error=EnriquecimientoPropiedadFallida, compensacion=RevertirEnriquecimientoPropiedad),
            #Transaccion(index=4, comando=HabilitarPropiedad, evento=PropiedadHabilitada, error=HabilitacionPropiedadFallida, compensacion=RevertirEnriquecimientoPropiedad),
            Fin(index=4)
            
        ]
        #Transaccion(index=2, comando=ValidarPropiedad, evento=PropiedadValidada, error=ValidacionPropiedadFallida, compensacion=RevertirValidacionPropiedad),
            #Transaccion(index=3, comando=EnriquecerPropiedad, evento=PropiedadEnriquecida, error=EnriquecimientoPropiedadFallida, compensacion=RevertirEnriquecimientoPropiedad),
            #Fin(index=4)

    def iniciar(self):
        print("Inicio")
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        print("Finalizo")
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        if evento.__class__ == PropiedadCreada:
            comando = ValidarPropiedad(id_propiedad = str(evento.id_propiedad))

        if evento.__class__ == EventoPropiedadValidada:
            comando = EnriquecerPropiedad(id_propiedad = str(evento.id_propiedad))

        # if evento.__class__ == PropiedadEnriquecida:
        #     comando = HabilitarPropiedad(id_propiedad = str(evento.id_propiedad))
        return comando

    def publicar_comando(self, evento: EventoDominio, tipo_comando: type):
        #print(evento.__class__)
        #print(PropiedadCreada.__class__)
        comando = self.construir_comando(evento, tipo_comando)
        ejecutar_commando(comando)

    def __init__(self):
        self.inicializar_pasos()

#el comando crear propiedad es por medio de API o desde la suscrión crear propiedad
#oir mensaje es de los eventos ... el primero que esta escuhando es PropiedadCreada
#el coordinador es el que se encarga de procesar el evento y ejecutar el comando
# el handler para oir mensaje deberìa ser evento propiedad creada .... 
from propiedadDeLosAlpes.seedwork.aplicacion.handlers import Handler

class HandlerSaga(Handler):
    @staticmethod    
    def oir_mensaje(evento):
        print("dispara oir mensaje")
        #print(evento)
        if isinstance(evento, EventoDominio):
            coordinador = CoordinadorPropiedades()
            coordinador.procesar_evento(evento)
        else:
            raise NotImplementedError("El mensaje no es evento de Dominio")
