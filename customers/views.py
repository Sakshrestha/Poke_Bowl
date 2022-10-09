from http.client import HTTPResponse
from random import random
from statistics import quantiles
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import AddOns, Cart, MenuItem, Category , AddOns,Offers, Order,Review
from .models import Cart as Product
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import OrderForm, UserRegistrationForm,ReviewForm
from django.http import JsonResponse,HttpResponseRedirect
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q

# Create your views here.

class Index(View):
    def get(self, request, *args , **kwasrgs):
        menu_items = MenuItem.objects.all()[:6]
        ingredients = AddOns.objects.all()
        offers = Offers.objects.all()
        context = {
            'menu_items' : menu_items,
            'ingredients':ingredients,
            'offers': offers,
        }
        return render(request, 'customers/index.html',context)

class About(View):
    def get(self, request, *args , **kwasrgs):
        return render(request, 'customers/about.html')

class Offers_view(View):
    def get(self, request, *args , **kwasrgs):
        offers= Offers.objects.all()
        context = {
            'offers' : offers,
        }
        return render(request, 'customers/offers.html',context)


class Menu(View):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        
        
        context = {
            'menu_items' : menu_items,
            
        }
        
        return render(request, 'customers/menu.html', context)

    def post(self, request):
        user = get_object_or_404(User, request.user)


class CartView(View):
    def get(self, request, *args , **kwasrgs):
        cart_items = Cart.objects.filter(user=request.user)
        item_count = cart_items.count()
        total_price = sum(items.items.price for items in cart_items )
        context = {
            'cart_items':cart_items,
            'item_count': item_count,
            'total_price': total_price,
        }

        return render(request, 'customers/add_to_cart.html',context)   

    def post(self, request, *args , **kwargs):
        cart = Cart.objects.get(user=request.user)
        form = OrderForm(request.POST)
        if form.is_valid():
            state = request.POST.get('state')
            city = request.POST.get('city')
            postal_code = request.POST.get('postal_code')
            order = Order(cart=cart, state=state,  city=city , postal_code=postal_code,is_payed=True)
            order.save()
            return render(request,'customers/index.html',{'alert':"Your order will be delivered soon."})

        return render(request, 'customers/add_to_cart.html')

class Product_description(View):
    def get(self, request,id):
        product=MenuItem.objects.get(id=id)
        ingredients = AddOns.objects.all()
        reviews = Review.objects.filter(menu=product)
        context = {
            'product':product,
            'ingredients' : ingredients,
            'reviews': reviews
            
        }
        
        return render(request,'customers/product_description.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('index')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'customers/register.html', context)

@login_required
def add_to_cart(request, id):
    item = get_object_or_404(MenuItem,id=id)
    cart = Cart.objects.create(user=request.user, items=item,price=item.price)
    cart.save()
    messages.success(request,'Added to cart')
    return redirect('cart')

@login_required
def remove_from_cart(request, id):
    Cart.objects.filter(id=id).delete()
    messages.success(request,'REmoved fromo cart')
    return redirect('cart')

@login_required
def rate(request, id):
    post = MenuItem.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        author = request.user
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        review = Review(author=author, stars = stars,  comment=comment , menu=post)
        review.save()
        return HttpResponseRedirect(reverse('product', args=(post.id,)))

    form = ReviewForm()
    context = {
        "form":form

    }

    return render(request, 'customers/rate.html',context)

class Dashboard(View):
    def get(self, request, *args , **kwargs):
        orders = Order.objects.all()
        context = {
            'orders':orders,
        }
        return render(request,'customers/dashboard.html',context)
    def post(self, request, *args , **kwargs):
        id= request.POST.get('id')
        order = Order.objects.get(id=id)
        delivered = request.POST.get('delivered')
        if delivered == "on":
            order.is_delivered =  True
            order.save()
        return redirect('dashboard')

def search(request):

    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'

        results = MenuItem.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query) )

    return render(request, 'customers/search_results.html', {'query': query, 'results': results})