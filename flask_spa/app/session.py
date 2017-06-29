from flask import session, request, redirect, url_for, escape

def create_app_session(app):

    # By default Flask implements sessions using a cryptographically signed cookie
    # and all user-session  data is serialized in the cookie

    # So choose a good secret-key
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    # Good way to generate a secret key - Copy/Paste the generated string
    # $ import os
    # $ os.urandom(24)

    @app.route('/protected')
    def protected():
        if 'username' in session:
            return 'Logged in as %s' % escape(session['username'])
        return 'You are not logged in'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('protected'))
        return '''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

    @app.route('/logout')
    def logout():
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('home'))
