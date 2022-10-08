"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import customers
from customers.views import CartView, Index, About, Menu,rate, Product_description,register,Offers_view,add_to_cart, remove_from_cart
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', Menu.as_view(), name='menu'),
    path('',Index.as_view(), name='index'),
    path('add/<int:id>',add_to_cart, name='add_to_cart'),
    path('remove/<int:id>',remove_from_cart, name='remove'),
    path('cart/',login_required(CartView.as_view()), name='cart'),
    path('about/',About.as_view(), name='about'),
    path('offers/',Offers_view.as_view(), name='offers'),
    path('rate/<int:id>',rate,name="rate"),
    path('product/<int:id>',Product_description.as_view(), name='product'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='customers/login.html'), name='login'),
    path('register/',register,name='register'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
