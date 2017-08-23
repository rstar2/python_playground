# Creating a Flask Single Page App


## Usage :

### One time
1. Create and activate a local python virtual environment
```bash
$ cd .
$ python -m venv env
$ source env/bin/activate   (for Windows - $ env\scripts\activate)python app.py
```

2. Install requirements later
```bash
$ pip install -r requirements.txt
```

### Each next time
1. Activate the local python virtual environment
```bash
$ source env/bin/activate   (for Windows - $ env\scripts\activate)python app.py
```

2. Run the server on http://127.0.0.1:5000/
```bash
$ python run.py 
```

3. Running/Debugging in VSCode is possible also with the _Flask_ launch task (just note that in that case the configuration parameter _DEBUG_ should be _False_)

3. For produccion environment (or any other) the default _Flask_ app configuration can be configured by setting an environment variable _APP_SETTINGS_ that point to a configuration file (like the _settings.cfg_ file - it's pure python inside)  

## To Add (Looking at https://github.com/realpython/flask-skeleton)

1. Flask
2. Flask-Bcrypt
3. Flask-Login
4. Flask-WTF
5. Flask-Migrate
6. Flask-Script
7. Flask-SQLAlchemy
8. Flask-Testing
9. coverage

