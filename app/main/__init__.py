from flask import Blueprint # type: ignore

main = Blueprint('main', __name__)

from . import routes, error # import routes and error handler

def create_app():
    # Create app function
    app = Flask(__name__) # type: ignore

    # Register main blueprint
    app.register_blueprint(main)

    return app