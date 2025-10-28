from flask import Blueprint

bp = Blueprint('api', __name__)

@bp.route('/some_route')
def some_route():
    return "Hello"
