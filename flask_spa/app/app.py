# import flask
from flask import Flask, render_template, request, make_response, url_for, jsonify

# initilize flask (with decorators)
app = Flask(__name__)

# setup the routes

# return a raw string
@app.route('/hello')
def hello():
    return "Hello, World!"

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

# get parameters from the request
# if path parameter is optionalthe 2 routes shoudl be set
# http://flask.pocoo.org/docs/0.10/quickstart/#routing
@app.route('/adder', methods=['GET', 'POST'])
@app.route('/adder/<int:init_value>', methods=['GET', 'POST'])
def adder(init_value=0):
    val = init_value
    if request.method == 'POST':
        # get POST form query params with the names as defined in the form
        # <form><input name="num1" .../> </form>
        num1 = int(request.form['num1'])

        # or as sent with Ajax data {num2: x, ....}
        num2 = int(request.form.get('num2'))

        val = val + num1 + num2

        # return JSON formatted data
        data = {'total': val}
        return jsonify(data)

    # with single kwargs
    return render_template('add.html', value=val)


@app.route('/cookie_get')
def cookie_get():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.

    return render_template('user.html', username=username)

@app.route('/cookie_set')
def cookie_set():
    # To access parameters submitted in the URL (?key=value) you can use the args attribute:
    username = request.args.get('username', '')

    resp = make_response(render_template('user.html', username=username))

    # set cookie
    resp.set_cookie('username', username)
    return resp

# Flask has default endpoint : static, and we cannot overwrite it
# @app.route('/static')
# def static():
#     pass



# run the server
if __name__ == '__main__':
    # debug=True - this also allows auto reloading if the app.py is changed
    app.run(debug=True)


