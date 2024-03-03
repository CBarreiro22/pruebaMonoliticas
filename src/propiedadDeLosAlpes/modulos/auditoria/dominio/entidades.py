from __future__ import annotations
from dataclasses import dataclass, field
from propiedadDeLosAlpes.modulos.auditoria.dominio.eventos import ResultadosValidacion

from propiedadDeLosAlpes.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Propiedad(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=None)
    
    def propiedad_modificada(self, propiedad: Propiedad):
        self.id_propiedad = propiedad.id_propiedad

@dataclass
class Auditoria(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=None)
    propietario: str = field(default=None)
    direccion: str = field(default=None)
    pais: str = field(default=None) 
    tipo_propiedad: str = field(default=None)   
    ubicacion: str = field(default=None)
    precio: str = field(default=None)
    id_empresa: str = field(default=None)
    superficie: str = field(default=None)
    estado: str = field(default=None)   
    
    def validar_propiedad(self, auditoria: Auditoria):
        for valor in auditoria.values():
            if valor == None:
                self.campos_faltantes.append(valor)
        if len(self.campos_faltantes) > 0:
            propiedad_validada = PropiedadModificada(id_propiedad=auditoria.id_propiedad, estado="faltan_datos", campos_faltantes=self.campos_faltantes)
        else:
            propiedad_validada=PropiedadModificada(id_propiedad=auditoria.id_propiedad, estado="exitoso", campos_faltantes=[])
        return propiedad_validada