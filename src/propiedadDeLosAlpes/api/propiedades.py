import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
from src.propiedadDeLosAlpes.seedwork.dominio.excepciones import ExcepcionDominio
from src.propiedadDeLosAlpes.seedwork.presentacion import api

app = api.crear_blueprint('propiedades', '/propiedades')


@app.route('/propiedades-comando', methods='POST')
def crear_propiedades():
    try:
        propiedad_dict = request.json
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
