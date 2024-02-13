from django.core.management import BaseCommand

from users.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        payment_list = [
            {"payment_amount": 500.0, "payment_method": 1},
            {"payment_amount": 1500.0, "payment_method": 2},
            {"payment_amount": 500.0, "payment_method": 1}
        ]

        for payment in payment_list:
            Payment.objects.create(**payment)
