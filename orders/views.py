from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order, robot_in_stock = form.save()
            if robot_in_stock:
                return HttpResponse(
                    "Этот робот у нас есть в наличии. Заказ успешно создан."
                )
            else:
                return HttpResponse(
                    "Заявка успешно создана! Мы уведомим вас по почте, когда робот станет доступен."
                )
    else:
        form = OrderForm()

    return render(request, 'create_order.html', {'form': form})
