from django import forms
from .models import Order
from orders.services import OrderService


class OrderForm(forms.ModelForm):
    customer_email = forms.EmailField(label='Email', max_length=255)
    robot_serial = forms.CharField(label='Серийный номер робота', max_length=5)

    class Meta:
        model = Order
        fields = ['customer_email', 'robot_serial']

    def save(self, commit=True):

        customer_email = self.cleaned_data['customer_email']
        robot_serial = self.cleaned_data['robot_serial']
        order, robot_in_stock = OrderService.create_order(customer_email, robot_serial)

        return order, robot_in_stock
