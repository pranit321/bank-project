from django.contrib import admin

# Register your models here.
from app.models import *

class customizebank(admin.ModelAdmin):
    search_fields=['bank_name']

class customizebranch(admin.ModelAdmin):
    list_display=['bank_name','ifsc','branch','address','contact','city','district','state']
    list_display_links=['ifsc']
    search_fields=['branch']

admin.site.register(Bank,customizebank)

admin.site.register(Branch,customizebranch)

