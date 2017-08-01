from flask import Flask

# Define the WSGI application object
app = Flask(__name__,
            template_folder='../client/templates',
            static_folder='../client/static')


# Configurations
# use this default ones

import os
if (os.getenv("VSCODE_DEBUG_FLASK", "False").lower() in ["true", "1"]):
    from .config import VSCDebugConfig as default_config
else:
    from .config import BaseConfig as default_config
app.config.from_object(default_config)
# or pass full module's path - app.config.from_object("app.server.config.BaseConfig")

# allow passing of real production configurations to modify/overwrite the default one
app.config.from_envvar('APP_SETTINGS', silent=True)

from flask_debugtoolbar import DebugToolbarExtension
DebugToolbarExtension(app)


# Define the database object which is imported
# by modules and controllers

# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy
# db = SQLAlchemy(app)
# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()

# Or use the app.config['DATABASE'] and app.config['DATABASE_CONNECT_OPTIONS']
db = None

# Main routing
from .main import *

# Auth routing (session based)
from .auth import *

# register the additional routes (Blueprints)
from .routes import routes
app.register_blueprint(routes)
