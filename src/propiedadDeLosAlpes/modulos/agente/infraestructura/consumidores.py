
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from propiedadDeLosAlpes.seedwork.infraestructura import utils
from propiedadDeLosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadRegistradaAgente
from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import EventoPropiedadCompletada
#from propiedadDeLosAlpes.modulos.agente.dominio.eventos import ResultadosValidacion
# from propiedadDeLosAlpes.modulos.agente.infraestructura.adaptadores import ServicioExternoPropiedades
# from propiedadDeLosAlpes.modulos.agente.dominio.entidades import Agente 
from pydispatch import dispatcher

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad-registrada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadDeLosAlpes-sub-eventos', schema=AvroSchema(EventoPropiedadRegistradaAgente))

        while True:
            mensaje = consumidor.receive()
            

            # #1.- Obtener id de la propiedad
            data=mensaje.value().data

            print(f'Evento recibido: {data}')

            # #2.- Consumir api rest de propiedad en capa infraestructura: GET /v1/propiedaes/{:id_propiedad}
            # servicio_propiedades = ServicioExternoPropiedades()
            # agente_propiedad_dict=servicio_propiedades.obtener_datos(id_propiedad=id_propiedad)
            id_propiedad = data.id_propiedad 
            lista_campos = data.campos_faltantes  
            payload = EventoPropiedadCompletada (id_propiedad=data.id_propiedad,  propiedades_completadas="isai oliva")
             

            # agente_propiedad_dto = map_agente.externo_a_dto(agente_propiedad_dict)
            # #3.- con la info de la api, se tiene que validar campos correctos en la capa de dominio
            
            # agente: agente = fabrica_agente.crear_objeto(agente_propiedad_dto, Mapeadoragente())
            # propiedad_validada=agente.validar_propiedad(agente)
            # #enviar evento con resultado de validación
            # evento_propiedad_modificada= ResultadosValidacion(id_propiedad=propiedad_validada.id_propiedad, estado=propiedad_validada.estado, campos_faltantes=propiedad_validada.campos_faltantes)
            dispatcher.send(signal=f'{type(payload).__name__}Dominio', evento=evento_propiedad_completada)
            
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()