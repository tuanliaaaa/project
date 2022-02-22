from re import search
from django.contrib import admin
from .models import Product,Transaction
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['ProductName','price']
    search_fields = ['ProductCode']
    list_filter = ['ProductName','price']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['UserName','quatily']
    raw_id_fields = ('Product',)
    search_fields = ['UserName']
    list_filter = ['UserName']
admin.site.register(Product,ProductAdmin)
admin.site.register(Transaction,TransactionAdmin)
