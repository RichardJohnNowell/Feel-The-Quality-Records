from django.contrib import admin
from .models import Product, Category

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
