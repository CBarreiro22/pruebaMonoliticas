import json
from flask import redirect, render_template, request, session, url_for
from flask import Response

from propiedadDeLosAlpes.modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedadDeLosAlpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from propiedadDeLosAlpes.seedwork.aplicacion.comandos import ejecutar_commando
from propiedadDeLosAlpes.seedwork.dominio.excepciones import ExcepcionDominio
from propiedadDeLosAlpes.seedwork.presentacion import api

app = api.crear_blueprint('propiedades', '/propiedades')


@app.route('/propiedades-comando', methods=['POST'])
def crear_propiedades():
    try:
        propiedad_dict = request.json
        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
        comando = CrearPropiedad (propiedad_dto.direccion, propiedad_dto.pais, propiedad_dto.tipo_propiedad, propiedad_dto.id, propiedad_dto.fecha_creacion, propiedad_dto.fecha_actualizacion)

        ejecutar_commando (comando)

        return Response('{}', status=202, mimetype='application/json')


    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
