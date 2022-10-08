from operator import le
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=32, verbose_name='Menu category name')
    description = models.CharField(max_length=128, verbose_name="Description about the item")

    class Meta:
        verbose_name='Menu Category'
        verbose_name_plural='Menu Categories'


class MenuItem(models.Model):
	
	name = models.CharField(max_length=48, help_text='Name of the item on the menu.')
	description = models.CharField(max_length=128, null=True, blank=True, help_text='The description is a simple text description of the menu item.')
	category = models.ManyToManyField(MenuCategory, verbose_name='menu category', help_text='Category is the menu category that this menu item belongs to, i.e. \'Appetizers\'.')
	price = models.IntegerField(help_text='The price is the cost of the item.')
	image = models.ImageField(upload_to='menu', null=True, blank=True, verbose_name='image', help_text='The image is an optional field that is associated with each menu item.')
	spicy = models.BooleanField(default=False, verbose_name='spicy?', help_text='Is this item spicy?')
	contains_peanuts = models.BooleanField(default=True, verbose_name='contain peanuts?', help_text='Does this item contain peanuts?')
	gluten_free = models.BooleanField(default=False, verbose_name='gluten free?', help_text='Is this item Gluten Free?')
	
	class Meta:
		verbose_name='menu item'
		verbose_name_plural='menu items'
		

	def __unicode__(self):
		return self.name

