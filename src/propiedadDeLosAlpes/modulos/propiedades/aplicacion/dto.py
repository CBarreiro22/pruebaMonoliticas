from dataclasses import dataclass

from src.propiedadDeLosAlpes.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class PropiedadDTO(DTO):
    direccion: str = fiel (default_factory=str)
    pais : str = fiel (default_factory=str)
    tipo_propiedad: str = fiel (default_factory=str)
    nombre_propietario: str = fiel (default_factory=str)
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)