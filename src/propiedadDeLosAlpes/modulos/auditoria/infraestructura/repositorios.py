
""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de propiedad

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de propiedad

"""

from propiedadDeLosAlpes.config.db import db
from propiedadDeLosAlpes.modulos.auditoria.dominio.repositorios import RepositorioAuditoria
from propiedadDeLosAlpes.modulos.auditoria.dominio.entidades import Auditoria
from propiedadDeLosAlpes.modulos.auditoria.dominio.fabricas import FabricaAuditoria
from .dto import Auditoria as AuditoriaDTO
from .mapeadores import MapeadorAuditoria
from uuid import UUID


class RepositorioAuditoriaPostgreSQL(RepositorioAuditoria):

    def __init__(self):
        self._fabrica_auditoria: FabricaAuditoria = FabricaAuditoria()

    @property
    def fabrica_auditoria(self):
        return self._fabrica_auditoria

    def obtener_por_id(self, id: UUID) -> Auditoria:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Auditoria]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Auditoria):
        auditoria_dto = self.fabrica_auditoria.crear_objeto(propiedad, MapeadorAuditoria())
        db.session.add(auditoria_dto)
        db.session.commit()
    
    def actualizar(self, propiedad: Auditoria):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        auditoria_dto = db.session.query(AuditoriaDTO).filter_by(id=str(propiedad_id)).first()
        if auditoria_dto is None:
            return
        db.session.delete(auditoria_dto)
        db.session.commit()