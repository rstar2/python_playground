from flask import render_template, request, make_response, jsonify

from . import routes

# setup the routes

# get path parameters from the request
# if path parameter is optionalt he 2 routes shoudl be set
# http://flask.pocoo.org/docs/0.10/quickstart/#routing
@routes.route('/adder', methods=['GET', 'POST'])
@routes.route('/adder/<int:init_value>', methods=['GET', 'POST'])
def adder(init_value=0):
    val = init_value

    # check if this is AJAX (POST) case
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


@routes.route('/cookie_get')
def cookie_get():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.

    return render_template('user.html', username=username)

@routes.route('/cookie_set')
def cookie_set():
    # To access parameters submitted in the URL (?key=value) you can use the args attribute:
    username = request.args.get('username', '')

    resp = make_response(render_template('user.html', username=username))

    # set cookie
    resp.set_cookie('username', username)
    return resp

