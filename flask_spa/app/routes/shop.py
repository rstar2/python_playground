import os
import time
import requests
import requests_cache

from flask import render_template, request, jsonify

import stripe

from . import routes

stripe_keys = {
    'secret_key': os.environ['SECRET_KEY'],
    'publishable_key': os.environ['PUBLISHABLE_KEY']
}

# initialize stripe
stripe.api_key = stripe_keys['secret_key']


@routes.route('/shop/<int:product_id>', methods=['GET'])
def shop(product_id):
    return render_template('shop.html', product_id=product_id, stripe_key=stripe_keys['publishable_key'])


@routes.route('/buy', methods=['POST'])
def buy(product_id):
    # Amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('thanks.html', product_id=product_id, amount=amount)