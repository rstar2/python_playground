import os
from flask import render_template, request

import stripe

from . import routes

stripe_keys = {
    'secret_key': "123123123",  # os.environ['SECRET_KEY'],
    # 'publishable_key': "123123123123123"  # os.environ['PUBLISHABLE_KEY']
    'publishable_key': ""
}

# initialize stripe
stripe.api_key = stripe_keys['secret_key']


@routes.route('/shop/<int:product_id>', methods=['GET'])
def shop(product_id):
    product_name = "Product ID"

    # Amount in cents
    product_price = 2342

    return render_template('shop.html', product_id=product_id,
                           product_name=product_name,
                           product_price=product_price,
                           stripe_key=stripe_keys['publishable_key'])


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
