from __future__ import annotations
from dataclasses import dataclass, field
from propiedadDeLosAlpes.modulos.auditoria.dominio.eventos import EventoPropiedadValidada

from propiedadDeLosAlpes.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Propiedad(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=None)
    
    def propiedad_modificada(self, propiedad: Propiedad):
        self.id_propiedad = propiedad.id_propiedad

@dataclass
class Auditoria(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=None)
    nombre_propietario: str = field(default=None)
    direccion: str = field(default=None)
    pais: str = field(default=None) 
    tipo_propiedad: str = field(default=None)   
    ubicacion: str = field(default=None)
    precio: str = field(default=None)
    id_empresa: str = field(default=None)
    superficie: str = field(default=None) 
    
    def validar_propiedad(self, auditoria: Auditoria):
        campos_faltantes=[]
        for nombre_propiedad, valor in auditoria.__dict__.items():
            if valor == None or valor =="":
                campos_faltantes.append(nombre_propiedad)
        if len(campos_faltantes) > 0:
            propiedad_validada = EventoPropiedadValidada(id_propiedad=auditoria.id_propiedad, estado="faltan_datos", campos_faltantes=campos_faltantes)
        else:
            propiedad_validada=EventoPropiedadValidada(id_propiedad=auditoria.id_propiedad, estado="exitoso", campos_faltantes=[])
        
        self.agregar_evento(propiedad_validada)
        return propiedad_validada