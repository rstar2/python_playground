from flask import render_template, request, make_response

from . import routes

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

