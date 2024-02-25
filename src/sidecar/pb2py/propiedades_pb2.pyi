from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Propiedad(_message.Message):
    __slots__ = ["direccion", "fecha_actualizacion", "fecha_creacion", "id", "pais", "propietario", "tipoPropiedad"]
    DIRECCION_FIELD_NUMBER: _ClassVar[int]
    FECHA_ACTUALIZACION_FIELD_NUMBER: _ClassVar[int]
    FECHA_CREACION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAIS_FIELD_NUMBER: _ClassVar[int]
    PROPIETARIO_FIELD_NUMBER: _ClassVar[int]
    TIPOPROPIEDAD_FIELD_NUMBER: _ClassVar[int]
    direccion: str
    fecha_actualizacion: _timestamp_pb2.Timestamp
    fecha_creacion: _timestamp_pb2.Timestamp
    id: str
    pais: str
    propietario: str
    tipoPropiedad: str
    def __init__(self, id: _Optional[str] = ..., propietario: _Optional[str] = ..., fecha_creacion: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., fecha_actualizacion: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., pais: _Optional[str] = ..., tipoPropiedad: _Optional[str] = ..., direccion: _Optional[str] = ...) -> None: ...

class RespuestaPropiedad(_message.Message):
    __slots__ = ["mensaje", "propiedad"]
    MENSAJE_FIELD_NUMBER: _ClassVar[int]
    PROPIEDAD_FIELD_NUMBER: _ClassVar[int]
    mensaje: str
    propiedad: Propiedad
    def __init__(self, mensaje: _Optional[str] = ..., propiedad: _Optional[_Union[Propiedad, _Mapping]] = ...) -> None: ...
