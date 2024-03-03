from .entidades import Auditoria
from dataclasses import dataclass
from propiedadDeLosAlpes.seedwork.dominio.fabricas import Fabrica
from propiedadDeLosAlpes.seedwork.dominio.repositorios import Mapeador
from propiedadDeLosAlpes.seedwork.dominio.entidades import Entidad
from .excepciones import TipoObjetoNoExisteEnDominioAuditoriasExcepcion

@dataclass
class _FabricaAuditoria(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            auditoria: Auditoria = mapeador.dto_a_entidad(obj)

            #self.validar_regla(MinimoUnItinerario(reserva.itinerarios))
            #[self.validar_regla(RutaValida(ruta)) for itin in reserva.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return auditoria

@dataclass
class FabricaAuditoria(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Auditoria.__class__:
            fabrica_auditoria = _FabricaAuditoria()
            return fabrica_auditoria.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioAuditoriasExcepcion()
