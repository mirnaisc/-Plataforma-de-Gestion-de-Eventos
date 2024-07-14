from flask import Blueprint

bp = Blueprint('usuarios_routes', __name__)

@bp.route('/usuarios')
def usuarios():
    return "Lista de usuarios"
