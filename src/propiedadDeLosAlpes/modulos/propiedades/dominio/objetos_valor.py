from enum import Enum


class EstadoPropiedad(str, Enum):
    AGREGADA = "Agregada"
    PENDIENTE = "Pendiente"
    FALLIDA = "Fallida"

class TipoPropiedad(str, Enum):
    MINORISTAS = "Minoristas"
    INDUSTRIAL = "Industrial"
    OFICINAS = "Oficinas"
    USO_ESPECIALIZADO = "USO Especialidade"

