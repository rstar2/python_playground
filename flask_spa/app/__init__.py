from flask import Flask


def create_db(app):
    # app.config['DATABASE']
    pass


def create_app(app):
    create_app_base(app)
    create_app_routes(app)

def create_app_base(app):
    from app import create_app_base
    create_app_base(app)
    
    from session import create_app_session
    create_app_session(app)


def create_app_routes(app):
    # register the additional routes (Blueprints)
    from routes import routes
    app.register_blueprint(routes)

# run the server
if __name__ == '__main__':
    # debug=True - this also allows auto reloading if the app.py is changed
    app = Flask(__name__)
    app.config.from_object(__name__)  # load config from this file , flaskr.py
    app.config.from_envvar('APP_SETTINGS', silent=True)

    create_db(app)
    create_app(app)

    # in order to debug in VSC it has to be started without debug=True
    # app.run(debug=True)
    app.run()
