from flask import Blueprint

bp = Blueprint('notificaciones_routes', __name__)

@bp.route('/notificaciones')
def notificaciones():
    return "Lista de notificaciones"
