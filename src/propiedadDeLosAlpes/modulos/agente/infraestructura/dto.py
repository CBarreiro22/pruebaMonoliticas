from propiedadDeLosAlpes.config.db import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, Numeric, Integer, ARRAY

import uuid

BaseAgente = declarative_base()


class PropiedadCompletada(BaseAgente):
    __tablename__ = "propiedades_completadas"
    id = Column(String, primary_key=True)
    campos_faltantes = Column(String)