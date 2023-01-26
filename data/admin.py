

# Register your models here.
from django.contrib import admin
from .models import Invetory
from .models import UploadCSV
# Register your models here.
class UploadCSVAdmin(admin.ModelAdmin):
    list_display = ['NewInv']
admin.site.register(Invetory)
admin.site.register(UploadCSV,UploadCSVAdmin)