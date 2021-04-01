from django.shortcuts import render
from django.views.generic import DetailView

from product.models import Product, Cart, ItemQuantity
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


def Items(request):
    # import ipdb; ipdb.set_trace()
    # cart_items = Cart.objects.prefetch_related('product').filter(author=request.user).first().product.all()
    items = Product.objects.all()

    return render(request, 'product/items.html', {'items': items})


@login_required
def cart(request):
    # import ipdb;ipdb.set_trace()
    try:
        my_cart = Cart.objects.filter(author=request.user).first().product.all()
    except:
        my_cart = ''
    print(my_cart)
    return render(request, 'product/cart.html', {'my_cart': my_cart})


@login_required
def add_to_cart(request, pk):
    # import ipdb;
    # ipdb.set_trace()
    # Quantity 1
    item = get_object_or_404(Product, pk=pk)
    order_item, created = ItemQuantity.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    if created:
        Cart.objects.filter(author=request.user).first().product.add(order_item)

    # Adding more quantity
    if not created:
        q1 = ItemQuantity.objects.filter(user=request.user).filter(item=pk).first()
        q1.quantity = q1.quantity + 1
        q1.save()
        print(q1)
    return redirect('home')
