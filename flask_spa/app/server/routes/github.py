import time
import requests
import requests_cache

from flask import render_template, request, jsonify

from . import routes

# set a SQLite cache for the requests
requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)


@routes.route('/github', methods=['GET', 'POST'])
def github():
    if request.method == 'POST':
        # user inputs
        loc = request.form.get('loc')
        lang = request.form.get('lang')
        # api call
        url = "https://api.github.com/search/users?q=location:{0}+language:{1}".format(loc, lang)
        now = time.ctime(int(time.time()))
        response = requests.get(url)
        print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))
        # return json
        return jsonify(response.json())
    return render_template('github.html')


