from propiedadDeLosAlpes.config.db import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, Numeric, Integer

import uuid

Base = declarative_base()

class Saga(Base):
    __tablename__ = "sagas"
    id = Column(String, primary_key=True)
    id_propiedad = Column(String)
    evento = Column(String)
    paso = Column(String)
    estatus = Column(String)
  