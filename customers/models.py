
from django.db import models
from django.conf import settings
from django.utils import timezone

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AddOns(models.Model):
    name = models.CharField(max_length=128)
    price =  models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    add_ons= models.ManyToManyField(AddOns)
    def __str__(self):
        return self.item.name



class Cart(models.Model):
    created_on = models.DateTimeField(default=timezone.now)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE,null=True)
    add_ons= models.ManyToManyField(AddOns)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return self.user.username


    

class Offers(models.Model):
    name=models.CharField(max_length=128)
    item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    updated_price=models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author = models.CharField(max_length=40)
    review_date = models.DateTimeField(default=timezone.now)
    rate_choices = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    stars = models.IntegerField(choices=rate_choices)
    comment = models.TextField(max_length=4000)
    menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu.name