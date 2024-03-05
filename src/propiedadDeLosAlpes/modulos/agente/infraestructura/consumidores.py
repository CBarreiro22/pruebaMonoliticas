
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from propiedadDeLosAlpes.seedwork.infraestructura import utils
from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import EventoPropiedadRegistrada
#from propiedadDeLosAlpes.modulos.agente.dominio.eventos import ResultadosValidacion
# from propiedadDeLosAlpes.modulos.agente.infraestructura.adaptadores import ServicioExternoPropiedades
# from propiedadDeLosAlpes.modulos.agente.dominio.entidades import Agente 
from pydispatch import dispatcher

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad-registrada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadRegistrada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            # #1.- Obtener id de la propiedad
            # id_propiedad = mensaje.value().data['id_propiedad']
            # #2.- Consumir api rest de propiedad en capa infraestructura: GET /v1/propiedaes/{:id_propiedad}
            # servicio_propiedades = ServicioExternoPropiedades()
            # agente_propiedad_dict=servicio_propiedades.obtener_datos(id_propiedad=id_propiedad)
            # map_agente = MapeadoragenteDTOJson()
            # agente_propiedad_dto = map_agente.externo_a_dto(agente_propiedad_dict)
            # #3.- con la info de la api, se tiene que validar campos correctos en la capa de dominio
            # fabrica_agente = Fabricaagente()
            # agente: agente = fabrica_agente.crear_objeto(agente_propiedad_dto, Mapeadoragente())
            # propiedad_validada=agente.validar_propiedad(agente)
            # #enviar evento con resultado de validación
            # evento_propiedad_modificada= ResultadosValidacion(id_propiedad=propiedad_validada.id_propiedad, estado=propiedad_validada.estado, campos_faltantes=propiedad_validada.campos_faltantes)
            # dispatcher.send(signal=f'{type(evento_propiedad_modificada).__name__}Dominio', evento=evento_propiedad_modificada)
            
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()