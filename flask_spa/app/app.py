from flask import render_template, redirect, url_for, make_response


def create_app_base(app):

    # return a template HTML
    # Flask will look for templates in the "templates" folder.
    # So if your application is a module, this folder is next to that module,
    # if it’s a package it’s actually inside your package:
    # Flask is using the Jinja2 templating language
    @app.route('/',)
    def home():
        # with dict expanded as kwargs
        context = {'value': "None"}
        return render_template('index.html', **context)

    # return a raw string
    @app.route('/hello')
    def hello():
        return "Hello, World!"

    # url_for(...) needs the name of the route function, NOT the URL
    # url_for('hello'), url_for('home'), url_for('routes.adder')

    # redirection to a route in the main app-route

    @app.route('/hello_redirect')
    def hello_redirect():
        return redirect(url_for('hello'))

    # redirection to a route in a Blueprint-route

    @app.route('/adder_redirect')
    def adder_redirect():
        return redirect(url_for('routes.adder'))

    # Flask has default endpoint : static, and we cannot overwrite it
    # @app.route('/static')
    # def static():
    #     pass

    # Error handling
    @app.errorhandler(404)
    def not_found(error):
        return render_template('error404.html'), 404

    @app.errorhandler(400)
    def bad_rquest(error):
        resp = make_response(render_template('error400.html'), 400)
        resp.headers['X-Something'] = 'A value'
        return resp

    from session import create_app_session
    create_app_session(app)
