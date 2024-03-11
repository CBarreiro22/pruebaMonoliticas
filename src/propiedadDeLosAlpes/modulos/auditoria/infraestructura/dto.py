from propiedadDeLosAlpes.config.db import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, Numeric, Integer

import uuid

Base = declarative_base()


class Auditoria(Base):
    __tablename__ = "auditoria"
    id = Column(String, primary_key=True)
    id_propiedad = Column(String)
    estado = Column(String)
    nombre_propietario: str = Column(String)
    direccion: str = Column(String)
    pais: str = Column(String)
    tipo_propiedad: str = Column(String)
    ubicacion: str = Column(String)
    id_empresa = Column(Integer)
    precio = Column(Numeric(precision=15, scale=2))
    superficie = Column(Numeric(precision=10, scale=2))
    estado: str = Column(String)

    