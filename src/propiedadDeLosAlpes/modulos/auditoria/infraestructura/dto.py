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

    