from __future__ import annotations
import uuid
from dataclasses import dataclass, field
import propiedadDeLosAlpes.modulos.propiedades.dominio.objetos_valor as ov
from propiedadDeLosAlpes.modulos.propiedades.dominio.eventos import PropiedadCreada
from propiedadDeLosAlpes.modulos.propiedades.dominio.comandos import ComandoValidarPropiedad
from propiedadDeLosAlpes.seedwork.dominio.entidades import AgregacionRaiz


@dataclass
class Propiedad(AgregacionRaiz):
    id_propietario: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoPropiedad = field(default=ov.EstadoPropiedad.PENDIENTE)
    tipo_propiedad: ov.TipoPropiedad = field(default=ov.TipoPropiedad.MINORISTAS)
    nombre_propietario: str = field(default=None)
    direccion: str = field(default=None)
    pais: str = field(default=None)
    tipo_propiedad: str = field(default=None)
    ubicacion: str = field(default=None)
    precio: float = field(default=0)
    id_empresa: int = field(default=0)
    superficie: float = field(default=0)
    estado: str = field(default=None)
 


    def crear_propiedad(self, propiedad: Propiedad):
        self.agregar_evento(
            ComandoValidarPropiedad(id_propiedad=self.id))