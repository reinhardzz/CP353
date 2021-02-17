from flask import current_app, Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template(current_app.config['INDEX_TEMPLATE'])



