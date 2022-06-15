from datetime import datetime, time, timedelta

from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware
from orders.models import Order

today = timezone.now()
tomorrow = today + timedelta(1)
today_start = make_aware(datetime.combine(today, time()))
today_end = make_aware(datetime.combine(tomorrow, time()))


class Command(BaseCommand):
    help = "Send Today's Orders Report to Admins"

    def handle(self, *args, **options):

        if orders:=Order.objects.all():
            message = "".join(f"{order} \n" for order in orders)

            subject = (
                f"Order Report for {today_start.strftime('%Y-%m-%d')} "
                f"to {today_end.strftime('%Y-%m-%d')}"
            )

            mail_admins(subject=subject, message=message, html_message=None)

            self.stdout.write("E-mail Report was sent.")
        else:
            self.stdout.write("No orders confirmed today.")
