from django.contrib import admin
from .models import *

class Hadmin(admin.ModelAdmin):
    list_display=['hname','hprice','description']
# Register your models here.
admin.site.register(booking,Hadmin)