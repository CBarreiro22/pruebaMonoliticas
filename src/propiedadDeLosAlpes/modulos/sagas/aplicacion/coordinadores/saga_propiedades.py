from propiedadDeLosAlpes.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedadDeLosAlpes.modulos.propiedades.dominio.eventos import PropiedadCreada  
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import Comando
from propiedadDeLosAlpes.seedwork.dominio.eventos import EventoDominio


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
            Transaccion(index=2, comando=ValidarPropiedad, evento=PropiedadValidada, error=ValidacionPropiedadFallida, compensacion=RevertirValidacionPropiedad),
            Transaccion(index=3, comando=EnriquecerPropiedad, evento=PropiedadEnriquecida, error=EnriquecimientoPropiedadFallida, compensacion=RevertirEnriquecimientoPropiedad),
            Fin(index=4)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...

def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorPropiedades()
        coordinador.procesar_evento(mensaje)
        print("oir mensaje")
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
