from functools import wraps
from flask import session, request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'logged_in' is session or not session.logged_in is True:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
