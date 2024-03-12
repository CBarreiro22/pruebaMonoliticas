import json
from flask import redirect, render_template, request, session, url_for
from flask import Response, jsonify

from propiedadDeLosAlpes.seedwork.presentacion import api

app = api.crear_blueprint('auditoria', '/auditoria')
