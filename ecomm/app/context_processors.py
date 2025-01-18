from .models import Cart

def total_items(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return {'totalitem': totalitem}
