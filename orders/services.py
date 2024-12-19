from customers.models import Customer
from django.core.mail import send_mail
from django.conf import settings
from robots.models import Robot
from orders.models import Order


class OrderService:
    @staticmethod
    def process_robot_availability(robot_serial):
        robot = Robot.objects.filter(serial=robot_serial, sold=False).first()
        if robot:
            order = Order.objects.filter(robot_serial=robot_serial, status='waiting').first()

            if order:
                order.status = 'fulfilled'
                order.save()

                send_mail(
                    subject=f"Ваш заказ на робота с серийным номером {robot_serial} теперь доступен",
                    message=(
                        f"Добрый день! \nНедавно вы интересовались нашим роботом "
                        f"модели {robot.model}, версии {robot.version}."
                        f"\n Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста,"
                        f" свяжитесь с нами"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[order.customer.email],
                )

                robot.sold = True
                robot.save()

    @staticmethod
    def create_order(customer_email, robot_serial):

        customer, _ = Customer.objects.get_or_create(email=customer_email)
        robot = Robot.objects.filter(serial=robot_serial, sold=False).first()
        order = Order.objects.create(
            customer=customer,
            robot_serial=robot_serial,
            status='fulfilled' if robot else 'waiting'
        )

        if robot:
            robot.sold = True
            robot.save()

        return order, bool(robot)
