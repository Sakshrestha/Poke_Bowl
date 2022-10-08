from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Offers)
admin.site.register(OrderItem)
admin.site.register(Review)