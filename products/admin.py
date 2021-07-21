from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'price', 'stock', )
    list_editable = ['price']
    list_filter = ['name', 'price']

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)