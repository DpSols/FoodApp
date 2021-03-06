from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Users)
admin.site.register(Order)
admin.site.register(Ingredients)
admin.site.register(Menu)
admin.site.register(Chief)
