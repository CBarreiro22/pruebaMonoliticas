from dataclasses import dataclass, field

from propiedadDeLosAlpes.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class PropiedadDTO(DTO):
    direccion: str = field(default_factory=str)
    pais : str = field(default_factory=str)
    tipo_propiedad: str = field(default_factory=str)
    nombre_propietario: str = field(default_factory=str)
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id_empresa: int = field(default_factory=int)
    superficie: float = field(default_factory=float)
    precio: float = field(default_factory=float)
    estado: str = field(default_factory=str)
    ubicacion: str = field(default_factory=str)