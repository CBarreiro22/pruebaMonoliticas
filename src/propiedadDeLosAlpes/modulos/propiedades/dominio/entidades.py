from __future__ import annotations
import uuid
from dataclasses import dataclass, field
import propiedadDeLosAlpes.modulos.propiedades.dominio.objetos_valor as ov
from propiedadDeLosAlpes.modulos.propiedades.dominio.eventos import PropiedadCreada
from propiedadDeLosAlpes.seedwork.dominio.entidades import AgregacionRaiz


@dataclass
class Propiedad(AgregacionRaiz):
    id_propietario: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoPropiedad = field(default=ov.EstadoPropiedad.PENDIENTE)
    tipo_propiedad: ov.TipoPropiedad = field(default=ov.TipoPropiedad.MINORISTAS)

    def crear_propiedad(self, propiedad: Propiedad):
        self.id_propietario = propiedad.id_propietario
        self.estado = propiedad.estado
        self.tipo_propiedad = propiedad.tipo_propiedad

        self.agregar_evento(
            PropiedadCreada(id_propiedad=self.id_propiedad, id_propietario=self.id_propietario, estado=self.estado.name,tipo_propiedad=self.tipo_propiedad,fecha_creacion=self.fecha_creacion))