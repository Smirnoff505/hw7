import stripe

from config import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_stripe_product(course_title):
    stripe_product = stripe.Product.create(name=course_title)
    return stripe_product['name']


def create_stripe_price(price, product_name):
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=price * 100,
        product_data={"name": product_name},
    )
    return stripe_price['id']


def create_stripe_session(stripe_price_id):
    stripe_session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": stripe_price_id, "quantity": 1}],
        mode="payment",
    )
    return stripe_session['url'], stripe_session['id']
