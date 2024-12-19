from django.test import TestCase, override_settings
from django.core import mail
from django.utils.timezone import now
from robots.models import Robot
from orders.models import Order
from customers.models import Customer


class SendEmailSignalTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            email="valishev57@mail.ru"
        )

        self.order = Order.objects.create(
            customer=self.customer,
            robot_serial="12345",
            status="waiting"
        )

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_email_sent_when_robot_with_serial_is_created(self):

        self.assertEqual(len(mail.outbox), 0)

        Robot.objects.create(
            serial="12345",
            model="R1",
            version="V1",
            created=now()
        )

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]

        self.assertEqual(
            email.subject,
            f"Ваш заказ на робота с серийным номером 12345 теперь доступен"
        )
        self.assertIn("Этот робот теперь в наличии", email.body)
        self.assertEqual(email.from_email, "valishev57@yandex.ru")
        self.assertEqual(email.to, [self.customer.email])

        self.order.refresh_from_db()
        self.assertEqual(self.order.status, "fulfilled")

    def test_email_not_sent_when_robot_serial_does_not_match(self):

        Robot.objects.create(
            serial="67890",
            model="R2",
            version="V2",
            created=now()
        )

        self.assertEqual(len(mail.outbox), 0)

        self.order.refresh_from_db()
        self.assertEqual(self.order.status, "waiting")
