from flask import Flask


def create_db():
    pass


def create_app():
    app = Flask(__name__)

    create_app_base(app)
    create_app_routes(app)

    return app

def create_app_base(app):
    from app import create_app_base
    create_app_base(app)

def create_app_routes(app):
    # register the additional routes (Blueprints)
    from routes import routes
    app.register_blueprint(routes)


    # run the server
if __name__ == '__main__':
    # debug=True - this also allows auto reloading if the app.py is changed
    db = create_db()
    app = create_app()

    # in order to debug in VSC it has to be started without debug=True
    # app.run(debug=True)

    app.run()
