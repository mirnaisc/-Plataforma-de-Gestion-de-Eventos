from flask import Blueprint

bp = Blueprint('registro_routes', __name__)

@bp.route('/registro')
def registro():
    return "Registro de usuarios"
