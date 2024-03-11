import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger
from sqlalchemy import create_engine
from sqlalchemy.orm import  scoped_session,sessionmaker
import asyncio

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))


def registrar_handlers():
    import propiedadDeLosAlpes.modulos.propiedades.aplicacion
    import propiedadDeLosAlpes.modulos.auditoria.aplicacion
    import propiedadDeLosAlpes.modulos.agente.aplicacion
    import propiedadDeLosAlpes.modulos.sagas.aplicacion


def importar_modelos_alchemy():
    import propiedadDeLosAlpes.modulos.propiedades.infraestructura.dto
    import propiedadDeLosAlpes.modulos.agente.infraestructura.dto
    #from propiedadDeLosAlpes.modulos.propiedades.infraestructura.dto import Propiedad
    #import propiedadDeLosAlpes.modulos.auditoria.infraestructura.dto


def comenzar_consumidor():
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """
    import threading
    import propiedadDeLosAlpes.modulos.propiedades.infraestructura.consumidores as propiedad
    import propiedadDeLosAlpes.modulos.auditoria.infraestructura.consumidores as auditoria
    import propiedadDeLosAlpes.modulos.agente.infraestructura.consumidores as agente

    # Suscripción a eventos
    threading.Thread(target=propiedad.suscribirse_a_eventos).start()
    threading.Thread(target=auditoria.suscribirse_a_eventos).start()
    threading.Thread(target=agente.suscribirse_a_eventos).start()
    

    # Suscripción a comandos
    threading.Thread(target=propiedad.suscribirse_a_comandos).start()


def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

    # Inicializa la DB
    from propiedadDeLosAlpes.config.db import init_db,database_connection
    app.config['SQLALCHEMY_DATABASE_URI'] = database_connection(configuracion, basedir=basedir)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #print(app.config['SQLALCHEMY_DATABASE_URI'])
    init_db(app)
    

    from propiedadDeLosAlpes.config.db import db
    importar_modelos_alchemy()
    registrar_handlers()

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    #from propiedadDeLosAlpes.modulos.propiedades.infraestructura.dto import Base
    from propiedadDeLosAlpes.modulos.agente.infraestructura.dto import Base
    Base.metadata.create_all(engine)
    db.session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    with app.app_context():
        try:
            db.create_all()
            #print("creada")
        except Exception as e:
            print(f"Error al crear la base de datos: {e}")
        if not app.config.get('TESTING'):
            comenzar_consumidor()

    
        from propiedadDeLosAlpes.modulos.sagas.aplicacion.coordinadores.saga_propiedades import CoordinadorPropiedades
        CoordinadorPropiedades()

    # Importa Blueprints
    from . import propiedades
    from . import agente

    # Registro de Blueprints
    app.register_blueprint(propiedades.app)
    app.register_blueprint(agente.app)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0.1"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health", methods=['GET'])
    def health():
        response = jsonify({"status": "up"})
        response.headers['Content-Type'] = 'application/json'
        return response

    return app