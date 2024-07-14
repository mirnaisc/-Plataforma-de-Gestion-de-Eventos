from flask import Blueprint

bp = Blueprint('eventos_routes', __name__)

@bp.route('/eventos')
def eventos():
    return "Lista de eventos"
