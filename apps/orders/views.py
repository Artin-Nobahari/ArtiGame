from django.shortcuts import render
from .forms import *

# Create your views here.
def check_out(request):
    cart = request.session.get("cart", {})
    products = Product.objects.all()
    if request.method == "PosT":
        form = OrderItem(request.POST)
        if form.is_valid():
            order = form.save()
            for x in products:
                quantity = cart.get(str(x.id, 0))
                orderItem.objects.create(order=Order, product=x, quantity=quantity)

            request.session['cart'] = {}
            return render(request, 'orders/order_success.html', {'order': order})
    
    else:
        form = OrderForm()
        return render(request, 'orders/.html', {'form': order, 'products': products, 'cart': cart})