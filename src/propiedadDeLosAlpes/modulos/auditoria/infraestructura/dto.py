from dataclasses import dataclass, field
from propiedadDeLosAlpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class AuditoriaDTO(DTO):
    id_propiedad: str = field(default_factory=str)
    nombre_propietario: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    pais: str = field(default_factory=str)
    tipo_propiedad: str = field(default_factory=str)
    ubicacion: str = field(default_factory=str)
    precio: str = field(default_factory=str)
    id_empresa: str = field(default_factory=str)
    superficie: str = field(default_factory=str)
    estado: str = field(default_factory=str) 