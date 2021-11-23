from flask import Flask
from google.appengine.api import wrap_wsgi_app

from backend.common.deferred.handlers import install_defer_routes
from backend.common.logging import configure_logging
from backend.common.middleware import install_middleware


configure_logging()

app = Flask(__name__)
app.wsgi_app = wrap_wsgi_app(app.wsgi_app)
install_middleware(app)
install_defer_routes(app)
