import time
import requests
import requests_cache

from flask import render_template, request, jsonify

from . import routes

# set a SQLite cache for the requests
requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)


@routes.route('/shop/<int:product_id>', methods=['GET'])
def shop(product_id):
    return render_template('shop.html', product_id=product_id)
