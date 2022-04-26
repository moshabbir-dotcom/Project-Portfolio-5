from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "The checkout basket is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KlDArKnrxwBRzWONPey1t5adCV9vzB57zhZRltDqOqrIjoYHFQBfcsq6psKFa5BRHOln7KZERI8BM2AIml0EaC300HyYEGIG1',
        'client_secret': 'test_client-secret',
    }

    return render(request, template, context)