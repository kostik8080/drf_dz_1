import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_KEYS


def create_stripe_course(instance):
    name_course_lesson = f"{instance.course}" if instance.course else f"{instance.lesson}"
    stripe_product = stripe.Product.create(
        name=f"{name_course_lesson}",
    )
    return stripe_product['id']


def create_stripe_price(product, product_id):
    """ Создает цену в Стрипе."""

    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=product * 100,
        product=product_id
    )
    return stripe_price['id']


def create_stripe_session(price):
    """ Создает сессию на оплату в Стрипе."""
    session = stripe.checkout.Session.create(
        success_url='http://127.0.0.1:8000/success',
        line_items=[{"price": price, "quantity": 1}],
        mode="payment",

    )
    return session.get('id'), session.get('url')
