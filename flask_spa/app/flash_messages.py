from flask import flash, redirect, render_template, \
    request, url_for

from .app import app

# The flashing system basically makes it possible to record a message
# at the end of a request and access it on the next (and only the next) request.
# This is usually combined with a layout template to expose the message.
# To flash a message use the flash() method, to get hold of the messages
# you can use get_flashed_messages() which is also available in the templates.

# the template index.html
# <!doctype html>
# <title>My Application</title>
# {% with messages = get_flashed_messages() %}
#   {% if messages %}
#     <ul class=flashes>
#     {% for message in messages %}
#       <li>{{ message }}</li>
#     {% endfor %}
#     </ul>
#   {% endif %}
# {% endwith %}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)