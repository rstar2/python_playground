from flask import session, flash, request, render_template, redirect, url_for, escape

from . import app

from .utils import login_required

# By default Flask implements sessions using a cryptographically signed cookie
# and all user-session data is serialized in the cookie
app.secret_key = app.config['SECRET_KEY']


@app.route('/protected')
@login_required
def protected():
    return 'Logged in as %s' % escape(session['username'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            error = 'Invalid username'
        elif request.form['password'] != 'admin':
            error = 'Invalid password'
        else:
            session['username'] = request.form['username']
            session['logged_in'] = True  # or just a simple flag
            flash('You were successfully logged in')
            # The '_next' param is needed for the login_required decorator
            _next = _next = request.form.get('_next', '')
            if (_next is ''):
                _next = url_for('home')
            return redirect(_next)
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))
