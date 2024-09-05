from flask import render_template # type: ignore
from . import main

# Error 404 Handler (Page Not Found)
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error 500 Handler (Internal Server Error)
@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500