import stripe
from flask import url_for

class Stripe():

    def __init__(self, secret_key):
        
        self.secret_key = secret_key


    def GetCheckoutFormUrl(self, Products, product_id, quantity=1):

        products = Products 
        if product_id not in products:
            abort(404)

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'product_data': {
                            'name': products[product_id]['name'],
                        },
                        'unit_amount': products[product_id]['price'],
                        'currency': 'usd',
                    },
                    'quantity': quantity,
                },
            ],
            payment_method_types=['card'],
            mode='payment',
            success_url=url_for('pincard.order_success', _external=True),
            cancel_url =url_for('pincard.order_fail', _external=True),        
        )

        return checkout_session.url



