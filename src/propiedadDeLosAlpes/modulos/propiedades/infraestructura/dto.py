from propiedadDeLosAlpes.config.db import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, Numeric, Integer

import uuid

Base = declarative_base()


class Propiedad(Base):
    __tablename__ = "propiedades"
    id = Column(String, primary_key=True)
    direccion = Column(String)
    pais = Column(String)
    tipo_propiedad = Column(String)
    nombre_propietario = Column(String)
    fecha_creacion = Column(DateTime, nullable=False)
    fecha_actualizacion = Column(DateTime, nullable=False)
    ubicacion = Column(String)
    estado = Column(String)
    id_empresa = Column(Integer)
    precio = Column(Numeric(precision=15, scale=2))
    superficie = Column(Numeric(precision=10, scale=2))