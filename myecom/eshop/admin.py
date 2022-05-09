from django.contrib import admin
from .models import Category, Products,Orders,Contact
# Register your models here.
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Contact)
admin.site.register(Category)