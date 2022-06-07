from django.contrib import admin
from .models import PenerimaanBarangHeader, PenerimaanBarangDetail


class DetailInline(admin.TabularInline):
    model = PenerimaanBarangDetail
    extra = 1
    classes = ['collapse']

    def has_delete_permission(self, request) -> bool:
        return False


class PenerimaanBarangAdmin(admin.ModelAdmin):
    list_filter = ['TrxInSuppIDf', 'TrxInDate'] 
    inlines = [DetailInline]


admin.site.register(PenerimaanBarangHeader, PenerimaanBarangAdmin)
