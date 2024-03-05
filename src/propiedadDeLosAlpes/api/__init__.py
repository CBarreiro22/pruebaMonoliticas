import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

from propiedadDeLosAlpes.modulos.agente.infraestructura.schema.v1.eventos import EventoPropiedadRegistrada

from src.propiedadDeLosAlpes.modulos.agente.infraestructura.despachadores import Despachador

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))


def registrar_handlers():
    import propiedadDeLosAlpes.modulos.propiedades.aplicacion
    import propiedadDeLosAlpes.modulos.auditoria.aplicacion


def importar_modelos_alchemy():
    import propiedadDeLosAlpes.modulos.propiedades.infraestructura.dto
    import propiedadDeLosAlpes.modulos.auditoria.infraestructura.dto


def comenzar_consumidor():
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """
    import threading
    import propiedadDeLosAlpes.modulos.propiedades.infraestructura.consumidores as propiedad
    import propiedadDeLosAlpes.modulos.auditoria.infraestructura.consumidores as auditoria

    # Suscripción a eventos
    threading.Thread(target=propiedad.suscribirse_a_eventos).start()
    threading.Thread(target=auditoria.suscribirse_a_eventos).start()

    # Suscripción a comandos
    threading.Thread(target=propiedad.suscribirse_a_comandos).start()


def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://user_propiedades:propiedades@localhost/propiedades'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

    # Inicializa la DB
    from propiedadDeLosAlpes.config.db import init_db
    init_db(app)

    from propiedadDeLosAlpes.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor()

    # Importa Blueprints
    from . import propiedades
    #from . import auditoria

    # Registro de Blueprints
    app.register_blueprint(propiedades.app)
    #app.register_blueprint(auditoria.app)

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

    @app.get("/prueba-propiedad-registrada", include_in_schema=False)
    async def prueba_propiedad_registrada() -> dict[str, str]:
        payload = EventoPropiedadRegistrada(id_propiedad="12345", campos_faltantes=["campo1", "campo2"])

        evento = EventoPropiedad(
            time=utils.time_millis(),
            ingestion=utils.time_millis(),
            datacontenttype=UsuarioValidado.__name__,
            usuario_validado=payload
        )
        despachador = Despachador()
        despachador.publicar_evento_propiedad_registrada(evento, "eventos-propiedad-registrada")
        return {"status": "ok"}

    return app
