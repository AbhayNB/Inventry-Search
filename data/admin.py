
# Register your models here.
from django.contrib import admin
from .models import Invetory
from .models import UploadCSV
from django.shortcuts import redirect
# Register your models here.
class InvetoryAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','Barcode','MRP','Rate_A']
    search_fields = ['Barcode']
def update_inventory(modeladmin, request, queryset):
    for obj in queryset:
        obj.update_inventory()
    return redirect("/admin/data/invetory/")

update_inventory.short_description = "Update Inventory for selected CSV"
class UploadCSVAdmin(admin.ModelAdmin):
    list_display = ['NewInv']
    actions = [update_inventory]
admin.site.register(Invetory,InvetoryAdmin)
admin.site.register(UploadCSV,UploadCSVAdmin)
admin.site.site_header = "Nari Comfort Wear: Admin"
