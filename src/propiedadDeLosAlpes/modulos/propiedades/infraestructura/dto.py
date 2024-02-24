from propiedadDeLosAlpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id = db.Column(db.String, primary_key=True)
    direccion = db.Column(db.String)
    pais :db.Column(db.String)
    tipo_propiedad:db.Column(db.String)
    nombre_propietario:db.Column(db.String)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)