from django.contrib import admin
from .models import Product, ProductStok
from django.http import HttpRequest



class StokAdmin(admin.ModelAdmin):

    search_fields = ['ProductIDF__ProductName']
    list_display = ('WarehouseIDF', 'ProductIDF', 'QtyDus', 'QtyPcs')
    list_filter = ['WarehouseIDF__WhsName'] 

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest) -> bool:
        return False


admin.site.register(Product)
admin.site.register(ProductStok, StokAdmin)