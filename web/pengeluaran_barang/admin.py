from django.contrib import admin
from .models import PengeluaranBarangHeader, PengeluaranBarangDetail


class DetailInline(admin.TabularInline):
    model = PengeluaranBarangDetail
    extra = 1
    classes = ['collapse']

    # def render_change_form(self, request, context, *args, **kwargs):
    #      context['adminform'].form.fields['TrxOutDProductIDF'].queryset = Theme.objects.filter(name__iexact='company')
    #      return super(CompanyAdmin, self).render_change_form(request, context, *args, **kwargs)


class PengeluaranBarangAdmin(admin.ModelAdmin):
    inlines = [DetailInline]


admin.site.register(PengeluaranBarangHeader, PengeluaranBarangAdmin)
