from flask import Blueprint, render_template
from flask import current_app as app
from flask_blueprint_tutorial.api import fetch_products


home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@home_bp.route('/', methods=['GET'])
def home():
    """Homepage."""
    products = fetch_products(app)
    return render_template(
        'index.jinja2',
        title='Flask Blueprint Demo',
        subtitle='Demonstration of Flask blueprints in action.',
        template='home-template',
        products=products
    )


@app.route('/')
def home():
    """Landing page."""
    nav = [
        {'name': 'Home', 'url': 'https://deniromovies.com/1'},
        {'name': 'About', 'url': 'https://deniromoviescore.com/2'},
        {'name': 'Pics', 'url': 'https://alldeniromoveis.com/3'}
    ]
    return render_template(
        'home.html',
        title="Deniro Movie Site",
        description="Deniro Movie score."
    )
