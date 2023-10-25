from flask import Blueprint, render_template_string

bp = Blueprint('site', __name__)


@bp.get('/')
def index():
    return render_template_string(
        """\
<h1> Olá, faça o login para usar o serviço.</h1>
<a href="{{ url_for('auth.login') }}">Login</a>
"""
    )
