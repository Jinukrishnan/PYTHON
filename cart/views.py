from django.shortcuts import render,redirect
from newapp.models import Product
from .models import Cart
# Create your views here.

def addCart(req,pid):
    if req.session["user"]=="":
         return redirect('credential:login')
    try:
        product=Product.objects.get(id=pid)
        print("pppp",product)
        user_id=req.session['user']
        cart_item=Cart.objects.get(product_id=product.id)
        if cart_item.quantity<cart_item.product.stock:
            cart_item.quantity+=1
            cart_item.save()
    except:
        cart_item=Cart.objects.create(product=product,quantity=1,user_id=user_id)
        cart_item.save()
       
    return redirect('cart:cart_details')

def cartDetails(req):

    user_id=req.session['user']
    
    cart=Cart.objects.all().filter(user_id=user_id)
    
    return render(req,'cart.html',{'cart':cart})