from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product

# Create your views here.
def view_basket(request):
    """ View to render the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add the quantity of a specific item to the users basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']
    basket = request.session.get('basket', {})

    if colour:
        if item_id in list(basket.keys()):
            if colour in basket[item_id]['items_by_colour'].keys():
                basket[item_id]['items_by_colour'][colour] += quantity
                messages.success(request,
                                 (f'Updated colour {colour.upper()} '
                                  f'{product.name} quantity to '
                                  f'{basket[item_id]["items_by_colour"][colour]}'))
            else:
                basket[item_id]['items_by_colour'][colour] = quantity
                messages.success(request,
                                 (f'Added colour {colour.upper()} '
                                  f'{product.name} to your shopping basket'))
        else:
            basket[item_id] = {'items_by_colour': {colour: quantity}}
            messages.success(request,
                             (f'Added colour {colour.upper()} '
                              f'{product.name} shopping basket'))
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {basket[item_id]}'))
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your shopping basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust quantity of a specific item to the new amount selected"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['items_by_colour'][colour] = quantity
            messages.success(request,
                             (f'Updated colour {colour.upper()} '
                              f'{product.name} quantity to '
                              f'{bag[item_id]["items_by_colour"][colour]}'))
        else:
            del basket[item_id]['items_by_colour'][colour]
            if not basket[item_id]['items_by_colour']:
                basket.pop(item_id)
            messages.success(request,
                             (f'Removed colour {colour.upper()} '
                              f'{product.name} from your shopping basket'))
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {basket[item_id]}'))
        else:
            basket.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your shopping basket'))

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove an item from basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        colour = None
        if 'product_colour' in request.POST:
            colour = request.POST['product_colour']
        basket = request.session.get('basket', {})

        if colour:
            del basket[item_id]['items_by_colour'][colour]
            if not basket[item_id]['items_by_colour']:
                basket.pop(item_id)
            messages.success(request,
                             (f'Removed colour {colour.upper()} '
                              f'{product.name} from your shopping basket'))
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your shopping basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)